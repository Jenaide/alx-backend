#!/usr/bin/env node
const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');
const bodyParser = require('body-parser');

const app = express();
const PORT = 1245;

// Create a Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Initialize available seats
setAsync('available_seats', 50);

// Initialize reservationEnabled flag
let reservationEnabled = true;

// Create a Kue queue
const queue = kue.createQueue();

// Middleware to parse JSON
app.use(bodyParser.json());

// Route to get the number of available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getAsync('available_seats');
  res.json({ numberOfAvailableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });
  
  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

// Route to process the queue and decrease available seats
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  const currentAvailableSeats = parseInt(await getAsync('available_seats'));
  
  if (currentAvailableSeats === 0) {
    reservationEnabled = false;
  }

  if (currentAvailableSeats >= 0) {
    queue.process('reserve_seat', async (job, done) => {
      const newAvailableSeats = await getAsync('available_seats');
      
      if (newAvailableSeats >= 1) {
        await setAsync('available_seats', newAvailableSeats - 1);
        done();
      } else {
        done(new Error('Not enough seats available'));
      }
    });
  }
});

app.listen(port, () => {
  console.log(`Server is listening on PORT ${PORT}`);
});

module.exports = app;

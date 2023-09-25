#!/usr/bin/env node
// imports
import { createClient } from 'redis';

const client = createClient();
const EXIT_MESSAGE = 'KILL_SERVER';


// error handling
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// subscribe to channel
client.subscribe('holberton school channel');

client.on('message', (_err, msg) => {
  console.log(msg);
  if (msg === EXIT_MESSAGE) {
    client.unsubscribe();
    client.quit();
  }
});

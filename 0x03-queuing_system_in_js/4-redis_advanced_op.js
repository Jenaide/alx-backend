#!/usr/bin/env node
// imports
import { createClient, print } from 'redis';

const client = createClient();


// error handling
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const updateHashing = (hashName, fieldName, fieldValue) => {
  client.hset(hashName, fieldName, fieldValue, print);
};

const printHashing = (hashName) => {
  client.hgetall(hashName, (_err, reply) => {
    console.log(reply);
  });
};

const main = () => {
  const hashedObj = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };
  for (const [field, value] of Object.entries(hashedObj)) {
    updateHashing('HolbertonSchools', field, value);
  }
  printHashing('HolbertonSchools');
};

// connection event
client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});

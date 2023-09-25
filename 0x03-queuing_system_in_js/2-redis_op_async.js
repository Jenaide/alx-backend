#!/usr/bin/env node
// imports
import { createClient, print } from 'redis';
import { promisify } from 'util';


// Create the redis client
const client = createClient();


// error handling
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// anonymous function to set new school value to redis
const setNewSchool = (schoolName, value) =>{
  client.SET(schoolName, value, print)
};

// anonymous function to display the school value from redis
const displaySchoolValue = async(schoolName) => {
  console.log(await promisify(client.GET).bind(client)(schoolName));
};

// call the functions
(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();

// connection event
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

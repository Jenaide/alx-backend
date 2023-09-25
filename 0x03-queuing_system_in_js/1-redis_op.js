#!/usr/bin/env node
import { createClient, print } from 'redis';


// Create the redis client
const client = createClient();


// connection event
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
// error handlin
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// anonymous function to set new school value to redis
const setNewSchool = (schoolName, value) =>{
  client.SET(schoolName, value, print)
};

// anonymous function to display the school value from redis
const displaySchoolValue = (schoolName) => {
  client.GET(schoolName, (_err, reply) => {
    console.log(reply);
  });
};

// call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

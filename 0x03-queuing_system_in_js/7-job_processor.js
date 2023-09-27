#!/usr/bin/yarn dev
import { createQueue } from 'kue';


const queue = createQueue();

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];


const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100); // starts the tracking progress

  if (blacklistedNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    let total = 2,
        pending = 2;

    const sendInterval = setInterval(() => {
      if (total - pending <= total / 2) {
        job.progress(total - pending, total);
      }

      if (total === pending) {
        console.log(
          `Sending notification to ${phoneNumber},`,
          `with message: ${message}`,
	);
      }

      --pending || done();
      pending || clearInterval(sendInterval);
    }, 1000);
  }
};

queue.progress('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

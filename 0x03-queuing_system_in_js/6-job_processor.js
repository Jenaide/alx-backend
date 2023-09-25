#!/usr/bin/env node
import { createQueue } from 'kue';


const queue = createQueue();


const sendNotification = (phoneNumber, message, job, done) => {
  const total = 2;
  let pending = total;
  const sendInterval = setInterval(() => {
    if (total - pending < total / 2) {
      job.progress(total - pending, total);
    }
    if (pending === 0) {
      clearInterval(sendInterval);
      console.log(
        `Sending notifiation to ${phoneNumber},`,
        `with message: ${message}`
      );
      done();
    }
    pending -= 1;
  }, 1000);
};

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

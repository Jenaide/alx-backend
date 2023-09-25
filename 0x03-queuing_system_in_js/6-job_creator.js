#!/usr/bin/env node
import { createQueue } from 'kue';


const queue = createQueue({ name: 'push_notification_code' });


const job = queue.create('push_notification_code', {
  phoneNumber: '0825536664',
  message: 'Account has been created',
});

job.on('queueing', () => {
  console.log('Notification job created:', job.id);
});

job.on('completed', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

job.save((err) => {
  if (!err) {
    console.log('Notification job created:', job.id);
  } else {
    console.error('Error creating notification job:', err);
  }
});

#!/usr/bin/env node
import { createQueue } from 'kue';
import sinon from 'sinon';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';


describe('createPushNotificationsJobs', () => {
  const spyWare = sinon.spy(console);
  const queue = createQueue({ name: 'push_notification_code_test' });

  before(() => {
    queue.testMode.enter(true);
  });

  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  afterEach(() => {
    spyWare.log.resetHistory();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(createPushNotificationsJobs.bind(createPushNotificationsJobs, {}, spyWare)).to.throw('Jobs is not an array');
  });

  it('should add a jobs to the queue with the correct type', (done) => {
    expect(spyWare.testMode.jobs.length).to.equal(0);
    const jobData = [
      {
        phoneNumber: '44556677889',
        message: 'Use the code 1982 to verify your account',
      },
      {
        phoneNumber: '98877665544',
        message: 'Use the code 1738 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobData, spyWare);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobData[0]);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    queue.process('push_notification_code_3', () => {
      expect(spyWare.log.calledWith('Notification job created:', spyWare.testMode.jobs[0].id)).to.be.true;
      done();
    });
  });

  it('should register the progress event handler for a job', (done) => {
    queue.testMode.jobs[0].addListener('progress', () => {
      expect(
        spyWare.log
          .calledWith('Notification job', queue.testMode.jobs[0].id, '25% complete')
      ).to.be.true;
      done();
    });
    queue.testMode.jobs[0].emit('progress', 25);
  });

  it('should register the failed event handler for a job', (done) => {
    queue.testMode.jobs[0].addListener('failed', () => {
      expect(
        spyWare.log
          .calledWith('Notification job', queue.testMode.jobs[0].id, 'failed:', 'Failed to send')
      ).to.be.true;
      done();
    });
    queue.testMode.jobs[0].emit('failed', new Error('Failed to send'));
  });

  it('should register the complete event handler for a job', (done) => {
    queue.testMode.jobs[0].addListener('complete', () => {
      expect(
        spyWare.log
          .calledWith('Notification job', queue.testMode.jobs[0].id, 'completed')
      ).to.be.true;
      done();
    });
    queue.testMode.jobs[0].emit('complete');
  });
});

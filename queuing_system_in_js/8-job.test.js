const kue = require('kue');
const { expect } = require('chai');
const createPushNotificationsJobs = require('./8-job');

describe('createPushNotificationsJobs', function () {
	const queue = kue.createQueue();

	before(function () {
		queue.testMode.enter();
	});

	after(function () {
		queue.testMode.clear();
		queue.testMode.exit();
	});

	it('should create two jobs in test mode', function () {
		const jobs = [
			{ phoneNumber: '4151237890', message: 'Hello 1' },
			{ phoneNumber: '4151237891', message: 'Hello 2' }
		];

		createPushNotificationsJobs(jobs, queue);

		expect(queue.testMode.jobs).to.have.lengthOf(2);
		expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
		expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
		expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
		expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
	});

	it('should throw an error when jobs is not an array', function () {
		expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
	});
});

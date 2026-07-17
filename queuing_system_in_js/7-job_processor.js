const kue = require('kue')
const newQueue = kue.createQueue()
newQueue.process('push_notification_code2', 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job , done)
})
const blackListedPhoneNumbers = [
    '4153518780',
    '4153518781'
]

function sendNotification(phoneNumber, message, job, done){
    job.progress(0,100)
    if (blackListedPhoneNumbers.includes(phoneNumber)){
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    else{
        job.progress(50, 100)
        console.log(`Sending notification to ${phoneNumber} with message ${message}`)
        done()
    }
}
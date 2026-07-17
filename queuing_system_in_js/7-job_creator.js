const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];
const { expect } = require('chai');
const e = require('express');
const kue = require('kue')
const newQueue = kue.createQueue()

jobs.forEach((job) =>{
  try{
    let newJob = newQueue.create('push_notification_code2', job)
    .save(()=>{
      console.log(`Notification job created: ${newJob.id}`)
    })
    newJob.on('complete',() =>{
      console.log(`Notification job ${newJob.id} completed`)
    })
    newJob.on('failed',(err) =>{
      console.log(`Notification job ${newJob.id} failed: ${err}`)
    })
    newJob.on('progress',(percent) =>{
      console.log(`Notification job ${newJob.id} ${percent}% complete`)
    })
  }
  catch (err){

  }
})

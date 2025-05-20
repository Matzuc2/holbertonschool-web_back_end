const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
});
process.stdin.setEncoding('utf8');
console.log('Welcome to Holberton School, what is your name?');
rl.on('line', (line) => {
  if (process.stdin.isTTY) {
    console.log(`Your name is: ${line}`);
    rl.close();
  } else {
    console.log(`Your name is: ${line}`);
    console.log('This important software is now closing');
    rl.close();
  }
});

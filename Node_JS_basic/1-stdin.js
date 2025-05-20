const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
});
console.log('Welcome to Holberton School, what is your name?');
rl.on('line', (line) => {
  if (process.stdin.isTTY) {
    console.log(`Your name is: ${line}`);
    process.exit(0);
  } else {
    console.log(`Your name is: ${line}`);
    console.log('This important software is now closing');
    rl.close();
  }
});

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
});
process.stdin.setEncoding('utf8');
process.stdout.write('Welcome to Holberton School, what is your name?\n');
rl.on('line', (line) => {
  if (process.stdin.isTTY) {
    if (line) {
      (process.stdout.write(`Your name is: ${line}\n`));
    }
    rl.close();
  } else {
    process.stdout.write(`Your name is: ${line}\n`);
    process.stdout.write('This important software is now closing\n');
    rl.close();
  }
});

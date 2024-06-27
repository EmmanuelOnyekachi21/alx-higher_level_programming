#!/usr/bin/node
/* Prints a square */
const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('Missing size');
}
const size = parseInt(args[0], 10);
if (!(isNaN(size))) {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      let line = '';
      for (let j = 0; j < size; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }
} else {
  console.log('Missing size');
}

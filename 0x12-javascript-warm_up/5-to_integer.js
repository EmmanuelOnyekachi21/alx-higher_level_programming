#!/usr/bin/node
/* prints My number: <first argument converted in integer> if the first argument can be converted to an integer: */
const args = process.argv.slice(2);
// parseInt requires the string to be converted to int and 10, i.e decimal
// when convert to binary, 2 = binary
const number = parseInt(args[0], 10);
if (!(isNaN(number))) {
  console.log('My number: ' + args[0]);
} else {
  console.log('Not a number');
}

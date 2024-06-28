#!/usr/bin/node

// Define a function to compute factorial recusrsively
function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

// Get the first command-line argument and convert it to an integer
const args = process.argv.slice(2);
const number = parseInt(args[0], 10);

// Compute the factorial using the defined function
const result = factorial(number);

// Print the result
console.log(result);

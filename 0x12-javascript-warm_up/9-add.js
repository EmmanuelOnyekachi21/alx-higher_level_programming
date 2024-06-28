#!/usr/bin/node

// Define the add function to add two numbers and print the result
function add (a, b) {
  const c = a + b;
  console.log(c);
}

// Get command-line arguments (excluding the first two which are 'node'
// and the script name
const args = process.argv.slice(2);

// Assign argumebts to variabes
let num1 = args[0];
let num2 = args[1];

// Convert arguments to integers
num1 = parseInt(num1, 10);
num2 = parseInt(num2, 10);

// Check if both arguments are valied numbers
if (!(isNaN(num1)) && !(isNaN(num2))) {
  add(num1, num2); // Call the add function with the parsed numbers
} else {
  console.log('NaN'); // Print 'NaN' if either argument is not a number
}

#!/usr/bin/node

// Initialize a global variable count to keep track of the number of times
// `logMe has been called
let count = 0;

/**
 * logMe - logs the number of arguments
 *          already printed and the 
 *          new argument value.
 * @param {*} item - The item to be logged.
 */
exports.logMe = function (item) {
  // Print the current count followed by the item
  console.log(`${count}: ${item}`);
  // Increment the count for the next call
  count++;
};

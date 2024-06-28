#!/usr/bin/node

// Function to manually sort an array in ascending order
function manualSort (array) {
  let i, j;

  for (i = 0; i < args.length; i++) {
    for (j = i + 1; j < args.length; j++) {
      if (args[i] > args[j]) {
        const temp = array[i];
        array[i] = array[j];
        array[j] = temp;
      }
    }
  }
  return array;
}

// Get command-line argumnets (excluding the first two)
// map(Number) is used to convert all arguments to integers
const args = process.argv.slice(2).map(Number);

// Check if there are no arguments or only one argument
if (args.length < 2) {
  console.log('0');
} else {
  // Manually sort the array in ascending order
  manualSort(args);

  // Print the second to last integer in the sorted array
  console.log(args[args.length - 2]);
}

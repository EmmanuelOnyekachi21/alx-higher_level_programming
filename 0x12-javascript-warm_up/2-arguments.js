#!/usr/bin/node
/* Prints a message depending on the number of arguments passed. */
const args = process.argv; // FIrst two argument in process.argv is #!/usr/bin/node and name of file
if (args.length <= 2) {
  console.log('No argument');
} else if (args.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

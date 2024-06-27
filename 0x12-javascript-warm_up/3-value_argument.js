#!/usr/bin/node
/* prints the first argument passed to it: */
const args = process.argv.slice(2);
// FIrst two argument in process.argv is #!/usr/bin/node and name of file
// Slicing focuses on  the first argument.
if (!args[0]) {
  console.log('No argument');
} else {
  console.log(args[0]);
}

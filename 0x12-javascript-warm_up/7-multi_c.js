#!/usr/bin/node
/* prints x times “C is fun” */
const args = process.argv.slice(2);
if (args.length <= 0) {
  console.log('Missing number of occurrences');
}
const isString = 'C is fun';
const isNum = Number(args[0]);
if (!(isNaN(isNum))) {
  if (isNum > 0) {
    for (let i = 0; i < isNum; i++) {
      console.log(isString);
    }
  }
}

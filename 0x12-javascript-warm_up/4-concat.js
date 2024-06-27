#!/usr/bin/node
/*
 * prints two arguments passed to it, in the following format: “ is ”
 */
isString = ' is ';
args = process.argv.slice(2);
console.log(args[0] + isString + args[1]);

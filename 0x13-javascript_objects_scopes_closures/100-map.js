#!/usr/bin/node

// Imports the list array from 100-data.js
const { list } = require('./100-data');

// Compute a new array using map
const mappedList = list.map((value, index) => value * index);

// Print the initial list
console.log(list);

// Print the new mapped list
console.log(mappedList);

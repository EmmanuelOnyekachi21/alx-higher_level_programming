#!/usr/bin/node

/**
 * This script imports a dictionary of occurences by key from a file
 * and computes a new dictionary where:
 * - The keys are the number of occurences.
 * - The values are arrays of user IDs that have those occurences.
 * The resulting dictionary is then printed.
 */

// IMport the dictionary from the file 101-data.js
const { dict } = require('./101-data');

/**
 * Initialize an empty object to store the new dictionary.
 * Keys will be the number of occurences, and values will be the array of keys
 */
const newDict = {};

for (let key in dict) {
  let occurence = dict[key];

  if (!newDict[occurence]) {
    newDict[occurence] = [];
  }

  newDict[occurence].push(key);
}

console.log(newDict);

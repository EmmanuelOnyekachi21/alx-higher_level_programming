#!/usr/bin/node

/**
 * nbOccurences - Returns the number of occurences in a list.
 *
 * @param {Array} list - The list to search through.
 * @param {*} searchElement - The element to count in the list.
 *
 * @returns {number} - The number of occurences of searchElement in the list.
 */
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      counter++;
    }
  }
  return counter;
};

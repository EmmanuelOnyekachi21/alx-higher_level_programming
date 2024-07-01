#!/usr/bin/node

/**
 * esrever - Returns the reversed version of a list
 *
 * @param {Array} list - The list to be reversed
 * @returns {Array} - the reversed versio of the list
 */
exports.esrever = function (list) {
  const newArr = [];
  const length = list.length;
  for (let i = length, j = 0; i > 0 && j < length; i--, j++) {
    newArr[j] = list[i - 1];
  }
  return newArr;
};

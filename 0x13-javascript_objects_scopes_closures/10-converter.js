#!/usr/bin/node

/**
 * Returns a function that converts a number from base 10 to the specified base
 * @param {number} base - The base to convert to.
 * @returns {function} - A function that takes a number
 *                        and returns its string representation.
 */
exports.converter = function (base) {
  function numberConvert (number) {
    return number.toString(base);
  }
  return numberConvert;
};

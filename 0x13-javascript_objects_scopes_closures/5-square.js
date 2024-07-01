#!/usr/bin/node
// A class `Square` that defines a square and inherits from Rectangle of 4-rectangle.js

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  /**
   * constructor for Square class.
   * @param {number} size - size of the square (both width and height).
   */
  constructor (size) {
    // Call the constructor of Rectangle with size for both width and height
    super(size, size);
  }
};

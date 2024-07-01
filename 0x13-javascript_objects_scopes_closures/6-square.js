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

  /**
   * Print the square using the specified character or 'X' by default.
   * @param {string} c - Character to use for priinting (default is 'X').
   */
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let line = '';
      for (let j = 0; j < this.height; j++) {
        line += c;
      }
      console.log(line);
    }
  }
};

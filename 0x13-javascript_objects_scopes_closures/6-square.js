#!/usr/bin/node
// A class `Square` that defines a square and inherits from Rectangle of 4-rectangle.js

const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {
  /**
   * Square class that inherits from OldSquare.
   * @param {number} size - size of the square (both width and height).
   */
  constructor (size) {
    // Call the constructor of OldSquare with size for both width and height
    super(size);
  }

  /**
   * Print the square using the specified character or 'X' by default.
   * @param {string} c - Character to use for priinting (default is 'X').
   */
  charPrint (c) {
    if (c === undefined) {
      c = 'X'; // Default character
    }

    // Print the square using the character c
    for (let i = 0; i < this.width; i++) {
      let line = '';
      for (let j = 0; j < this.height; j++) {
        line += c;
      }
      console.log(line);
    }
  }
};

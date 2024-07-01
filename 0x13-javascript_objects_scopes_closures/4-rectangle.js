#!/usr/bin/node
/* A class `Rectangle` that defines a rectangle */

module.exports = class Rectangle {
  // constructor with width (w) and height (h) parameters

  constructor (w, h) {
    // Initialize instance attributes width and height if both are greater than 0
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /**
   * Print the rectangle using 'X'.
   */
  print () {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  /**
   * Rotate the rectangle by exchanging width and height.
   */
  rotate () {
    let temp = this.height;
    this.height = this.width;
    this.width = temp;
  }
  
  /**
   * Double the dimensions (width and height) of the rectangle.
   */
  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
};

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

  print () {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }
};

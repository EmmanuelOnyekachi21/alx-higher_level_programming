#!/usr/bin/node
/* A class `Rectangle` that defines a rectangle */

class Rectangle {
  // constructor with width (w) and height (h) parameters

  constructor (w, h) {
    // Check if width or height is not a positive integer or zero
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      // Return an empty object if invalid dimensions are provided
      return {};
    } else {
      // Initialize instance attributes width and height
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;

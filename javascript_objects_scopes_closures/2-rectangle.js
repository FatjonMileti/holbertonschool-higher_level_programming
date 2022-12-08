#!/usr/bin/node
// Write an empty class Rectangle that defines a rectangle.

class Rectangle {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;

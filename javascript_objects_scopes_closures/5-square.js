#!/usr/bin/node
// Write an empty class Rectangle that defines a rectangle.

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;

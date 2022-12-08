#!/usr/bin/node
// Write an empty class Rectangle that defines a rectangle.

const sq1 = require('./5-square');

class Square extends sq1 {
}

Square.prototype.charPrint = function (c) {
  if (!c) {
    c = 'X';
  }
  for (let i = 0; i < this.width; i++) {
    console.log(c.repeat(this.width));
  }
};

module.exports = Square;

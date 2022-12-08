#!/usr/bin/node
// Write an empty class Rectangle that defines a rectangle.

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};

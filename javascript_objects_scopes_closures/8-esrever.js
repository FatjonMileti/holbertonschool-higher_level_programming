#!/usr/bin/node
// Write an empty class Rectangle that defines a rectangle.

exports.esrever = function (list) {
  const reversed = [];
  for (const item of list) {
    reversed.unshift(item);
  }
  return reversed;
};

#!/usr/bin/node
// Write an empty class Rectangle that defines a rectangle.

exports.nbOccurences = function (list, searchElement) {
  let noccur = 0;
  for (const item of list) {
    if (item === searchElement) {
      noccur++;
    }
  }
  return noccur;
};

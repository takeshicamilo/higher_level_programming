#!/usr/bin/node
// poor

exports.nbOccurences = function (list, searchElement) {
  let temp = 0;
  for (let x = 0; x < list.length; x++) {
    if (list[x] === searchElement) {
      temp++;
    }
  }
  return temp;
};

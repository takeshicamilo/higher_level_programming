#!/usr/bin/node
// log
let count = 0;
exports.logMe = function (item) {
  console.log('%d: %s', count, item);
  count++;
};

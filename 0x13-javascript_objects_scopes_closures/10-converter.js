#!/usr/bin/node
// sha sha
exports.converter = function (base) {
  return function mainConvert (num) {
    return num.toString(base);
  };
};

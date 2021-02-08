#!/usr/bin/node
// lel

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  charPrint (c) {
    this.print(c);
  }
};

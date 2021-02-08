#!/usr/bin/node
// xdd
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && h != null && w != null) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  }
};

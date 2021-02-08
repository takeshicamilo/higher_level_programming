#!/usr/bin/node
// xdddd

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && h != null && w != null) {
      this.width = w;
      this.height = h;
    }
  }

  print (x) {
    let value = 'X';
    if (x) {
      value = x;
    }
    for (let x = 0; x < this.height; x++) {
      console.log(value.repeat(this.width));
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
};

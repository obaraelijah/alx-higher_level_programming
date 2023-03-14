#!/usr/bin/node

module.exports = class Rectangle {
  constructor (h, w) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += 'x';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
};

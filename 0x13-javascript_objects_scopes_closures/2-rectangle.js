#!/usr/bin/node

module.exports = class Rectangle {
  constructor (h, w) {
    if (h <= 0 && w <= 0) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
};

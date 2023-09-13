#!/usr/bin/node
/* class Rectangle definition */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let idy;
    for (idy = 0; idy < this.height; idy++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;

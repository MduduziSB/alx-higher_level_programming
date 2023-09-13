#!/usr/bin/node
/* class Square definition */

const SQUARE = require('./5-square');
class Square extends SQUARE {
  charPrint (c) {
    if (c == null) {
      c = 'X';
    }
    for (let idx = 1; idx <= this.height; idx++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;

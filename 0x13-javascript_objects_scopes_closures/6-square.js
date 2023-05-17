#!/usr/bin/node
const SquareClass = require('./5-square');
class Square extends SquareClass {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let res = '';
      for (let j = 0; j < this.width; j++) {
        if (c !== undefined) {
          res += c;
        } else {
          res += 'X';
        }
      }
      console.log(res);
    }
  }
}

module.exports = Square;

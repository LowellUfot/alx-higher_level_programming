#!/usr/bin/node
const SquareClass = require('./5-square');
class Square extends SquareClass {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      let res = '';
      for (let j = 0; j < this.size; j++) {
        if (typeof (c) !== 'undefined') {
          res += 'c';
        } else {
          res += 'X';
        }
      }
      console.log(res);
    }
  }
}

module.exports = Square;

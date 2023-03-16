#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    if (c && String.isString(c) && c.length == 1) {
      for (let i = 0; i < this.height; i++) {
        let str = '';
        for (let j = 0; j < this.width; j++) {
          str += c;
        }
        console.log(str);
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;

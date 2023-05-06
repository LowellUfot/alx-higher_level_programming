#!/usr/bin/node
const process = require('process');
const argv = process.argv;

if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  let i = argv[2];
  let str = '';
  while (i > 0) {
    for (let j = 0; j < argv[2]; j++) {
      str += 'X';
    }
    console.log(str);
    str = '';
    i--;
  }
}

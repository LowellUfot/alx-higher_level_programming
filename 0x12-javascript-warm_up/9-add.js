#!/usr/bin/node
const process = require('process');
const argv = process.argv;

if (isNaN(argv[2]) || isNaN(argv[3])) {
  console.log('NaN');
} else {
  add(parseInt(argv[2]), parseInt(argv[3]));
}

function add (num1, num2) {
  console.log(num1 + num2);
}

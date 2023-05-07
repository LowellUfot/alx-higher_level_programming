#!/usr/bin/node
const process = require('process');
const argv = process.argv;

if (isNaN(argv[2])) {
  console.log(1);
} else {
  console.log(factorial(parseInt(argv[2])));
}

function factorial (num) {
  if (num === 0 || num === 1) {
    return (1);
  }
  return (num * factorial(num - 1));
}

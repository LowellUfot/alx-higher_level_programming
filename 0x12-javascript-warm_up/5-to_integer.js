#!/usr/bin/node
const process = require('process');

const argv = process.argv;

const myNum = +argv[2];
// print process.argv
if (isNaN(myNum)) {
  console.log('Not a number');
} else if (typeof (myNum) === 'number') {
  console.log(`My number: ${myNum}`);
} else {
  console.log('Not a number');
}

#!/usr/bin/node
const process = require('process');
const argv = process.argv;

if (isNaN(argv[2])) {
  console.log('Missing number of occurencies');
} else {
  for (let j = 0; j < argv[2]; j++) {
    console.log('C is fun');
  }
}

#!/usr/bin/node
const process = require('process');

const argv = process.argv;

// print process.argv
if (argv[2] !== undefined) {
  console.log(`${argv[2]}`);
} else {
  console.log('No argument');
}

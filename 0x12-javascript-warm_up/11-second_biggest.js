#!/usr/bin/node
const process = require('process');

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const argv = process.argv.slice(2);
  console.log(secondBiggest(argv));
}

function secondBiggest (arr) {
  if (arr.length <= 1) {
    console.log(0);
    return;
  }

  let biggest = 0;
  let secondBiggest = 0;

  for (let i = 0; i < arr.length; i++) {
    const num = parseInt(arr[i]);
    if (num > biggest) {
      secondBiggest = biggest;
      biggest = num;
    } else if (num > secondBiggest && num < biggest) {
      secondBiggest = num;
    }
  }

  return secondBiggest;
}

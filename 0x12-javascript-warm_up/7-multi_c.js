#!/usr/bin/node

const arg = process.argv[2];
const intval = parseInt(arg);
let i = 0;
if (!isNaN(intval)) {
  while (i < intval) {
    console.log('c is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}

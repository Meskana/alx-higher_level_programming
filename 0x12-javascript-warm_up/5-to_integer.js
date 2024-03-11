#!/usr/bin/node

const arg = process.argv[2];
const result = parseInt(arg);
if (!isNaN(result)) {
  console.log('My number:', result);
} else {
  console.log('Not a number');
}

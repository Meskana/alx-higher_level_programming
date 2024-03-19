#!/usr/bin/node

const arg = process.argv[2];
const result = parseInt(arg);
if (!isNaN(result)) {
  for (let i = 0; i < result; i++) {
    let row = '';
    for (let j = 0; j < result; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}

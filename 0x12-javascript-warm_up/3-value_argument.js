#!/usr/bin/node

let count = 0;
let val = '';
process.argv.forEach((arg, index) => {
  if (index >= 2) {
    count++;
    val = arg;
  }
});

if (count === 0) {
  console.log('No argument');
} else {
  console.log(`${val}`);
}

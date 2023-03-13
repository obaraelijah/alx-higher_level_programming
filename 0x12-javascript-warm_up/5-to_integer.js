#!/usr/bin/node

const arg = process.argv[2];
const num = parseInt(arg); // converts  argument to n integer

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}

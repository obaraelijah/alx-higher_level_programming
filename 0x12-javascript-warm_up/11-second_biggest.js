#!/usr/bin/node

const args = process.argv.slice(2);
const nums = args.map(Number);
const secondBiggest = Math.max(...nums.filter(num => num !== Math.max(...nums)));

console.log(nums.length <= 1 ? 0 : secondBiggest);

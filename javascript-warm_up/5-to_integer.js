#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg);

if (arg === undefined || isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}

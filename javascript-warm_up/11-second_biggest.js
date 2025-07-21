#!/usr/bin/node
const args = process.argv.slice(2);
const numbers = args.map(num => parseInt(num));
if (args.length <= 1) {
  console.log(0);
} else {
  const sorted = numbers.sort((a, b) => b - a);
  console.log(sorted[1]);
}

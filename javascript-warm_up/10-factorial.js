#!/usr/bin/node
const n = process.argv[2];
function factorial(n) {
  const num = parseInt(n);
  if (isNaN(num) || num <= 1) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(n));

#!/usr/bin/node
/* prints factorial of a number */

const argument = process.argv[2];
const n = parseInt(argument, 10);
function computeFactorial (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  }
  if (n === 0) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
}
console.log(computeFactorial(n));

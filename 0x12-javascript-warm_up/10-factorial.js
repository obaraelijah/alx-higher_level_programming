#!/usr/bin/node
/**
 * a script that computes and prints a factorial
 */
function factorial (n) {
  if (isNaN(n)) {
    return (1);
  } else if (n === 1 || n === 0) {
    return (1);
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(parseInt(process.argv[2])));

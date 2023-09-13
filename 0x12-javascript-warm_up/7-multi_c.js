#!/usr/bin/node
/* The script converts first argument to int */

const str = 'C is fun';
const argument = process.argv[2];
const parsedNumber = parseInt(argument, 10);
if (!isNaN(parsedNumber) && parsedNumber > 0) {
  for (let i = 0; i < parsedNumber; i++) {
    console.log(str);
  }
} else {
  if (argument == null) {
    console.log('Missing number of occurrences');
  }
}

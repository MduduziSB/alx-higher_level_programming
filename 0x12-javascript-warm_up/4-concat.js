#!/usr/bin/node
/* Prints passed arguments */

const process = require('process');
const args = process.argv;
const val = 'undefined';
let len = 0;
for (let i = 0; args[i]; i++) {
  len++;
}
if (len === 2) {
  console.log(`${val} is ${val}`);
} else if (len === 3) {
  console.log(`${args[2]} is ${val}`);
} else {
  console.log(`${args[2]} is ${args[3]}`);
}

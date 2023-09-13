#!/usr/bin/node
/* Prints passed arguments */

const process = require('process');
const args = process.argv;
let len = 0;
for (let i = 0; args[i]; i++) {
  len++;
}
if (len === 2) {
  console.log('No argument');
} else {
  console.log(args[2]);
}

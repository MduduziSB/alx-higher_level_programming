#!/usr/bin/node
/* the script prints a square */

const a = process.argv[2];
const b = process.argv[3];
function add (a, b) {
  if (a == null || b == null) {
    console.log('NaN');
  } else {
    console.log(parseInt(a, 10) + parseInt(b, 10));
  }
}
add(a, b);

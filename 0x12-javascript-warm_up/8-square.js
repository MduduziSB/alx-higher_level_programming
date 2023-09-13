#!/usr/bin/node
/* the script prints a square */

const size = process.argv[2];
if (isNaN(size) || size === undefined) {
  console.log('Missing size');
} else {
  const parsedSize = parseInt(size, 10);

  for (let i = 0; i < parsedSize; i++) {
    let row = '';
    for (let j = 0; j < parsedSize; j++) {
      row += 'X';
    }
    console.log(row);
  }
}

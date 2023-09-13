#!/usr/bin/node
/* The script uses a while loop to print 3 lines */

const arr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let i = 0;
while (arr[i]) {
  console.log(arr[i++]);
}

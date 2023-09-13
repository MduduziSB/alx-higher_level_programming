#!/usr/bin/node
/* prints arguments */

let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};

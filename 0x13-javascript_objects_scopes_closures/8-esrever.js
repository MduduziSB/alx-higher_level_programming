#!/usr/bin/node
/* function that reverses a list */

exports.esrever = function (list) {
  let fwd, tmp;
  fwd = 0;
  for (let i = list.length - 1; i > fwd; i--) {
    tmp = list[i];
    list[i] = list[fwd];
    list[fwd++] = tmp;
  }
  return (list);
};

#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const dict = {};

    for (let i = 0; i < data.length; i++) {
      const elem = data[i];
      if (!dict[elem.userId]) {
        if (elem.completed) {
          dict[elem.userId] = 1;
        }
      } else {
        if (elem.completed) {
          dict[elem.userId] += 1;
        }
      }
    }

    console.log(dict);
  }
});

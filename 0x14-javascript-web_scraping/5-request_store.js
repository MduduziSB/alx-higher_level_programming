#!/usr/bin/node
/* This script gets the contents of a webpage and stores it in a file */

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error Code:', response.statusCode);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(writeError);
      }
    });
  }
});

#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  }
  const films = JSON.parse(body).results;
  const Wedge_appearances = films.reduce((count, film) => {
    if (film.characters.some(character => character.endsWith(`/${characterId}/`))) {
      return count + 1;
    }
    return count;
  }, 0);

  console.log(Wedge_appearances);
});

#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error code: ' + response.statusCode);
  } else {
    const films = JSON.parse(body).results;
    const Wedge_appearances = films.filter(film => {
      return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);
    }).length;

    console.log(Wedge_appearances);
  }
});

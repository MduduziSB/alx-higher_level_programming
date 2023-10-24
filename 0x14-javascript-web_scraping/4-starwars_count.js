#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  }
  const films = JSON.parse(body).results;
  const url = 'https://swapi-api.alx-tools.com/api/people/';
  const Wedge_appearances = films.filter(film => {
    return film.characters.includes(`${url}${characterId}/`);
  }).length;

  console.log(Wedge_appearances);
});

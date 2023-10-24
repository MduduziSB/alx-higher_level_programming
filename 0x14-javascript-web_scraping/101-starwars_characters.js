#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

const movieURL = `https://swapi.dev/api/films/${movieId}/`;

request(movieURL, (error, response, movieBody) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(movieBody);
    const characters = movie.characters;
    let characterIndex = 0;

    const fetchCharacter = () => {
      if (characterIndex < characters.length) {
        const characterURL = characters[characterIndex];
        request(characterURL, (charError, charResponse, charBody) => {
          if (charError) {
            console.log(charError);
          } else {
            const character = JSON.parse(charBody);
            console.log(character.name);
            characterIndex++;
            fetchCharacter();
          }
        });
      }
    };

    fetchCharacter();
  }
});

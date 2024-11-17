#!/usr/bin/node
// This script prints all characters of a Star Wars movie
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node starwars_characters.js <MovieID>');
  process.exit(1);
}

const movieId = process.argv[2];
const options = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + movieId,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}

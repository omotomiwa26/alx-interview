#!/usr/bin/node
// This script prints all characters of a Star Wars movie
// const request = require('request');

// if (process.argv.length !== 3) {
//   console.error('Usage: node starwars_characters.js <MovieID>');
//   process.exit(1);
// }

// const movieId = process.argv[2];
// const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// request(apiUrl, (error, response, body) => {
//   if (error) {
//     console.error('Error fetching data:', error);
//     return;
//   }

//   if (response.statusCode !== 200) {
//     console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
//     return;
//   }

//   try {
//     const data = JSON.parse(body);
//     const characterUrls = data.characters;

//     characterUrls.forEach((url) => {
//       request(url, (charError, charResponse, charBody) => {
//         if (charError) {
//           console.error('Error fetching character data:', charError);
//           return;
//         }

//         if (charResponse.statusCode !== 200) {
//           console.error(
//             `Failed to fetch character data. Status code: ${charResponse.statusCode}`
//           );
//           return;
//         }

//         const character = JSON.parse(charBody);
//         console.log(character.name);
//       });
//     });
//   } catch (parseError) {
//     console.error('Error parsing data:', parseError);
//   }
// });

// script that prints all characters of a Star Wars movie:
const request = require('request');
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
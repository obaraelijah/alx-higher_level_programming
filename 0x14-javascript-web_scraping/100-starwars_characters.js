#!/usr/bin/node
const request = require('request');

const starWarsUri = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(starWarsUri, (_err, _res, body) => {
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++i) {
    request(characters[i], function (_cErr, _cRes, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});


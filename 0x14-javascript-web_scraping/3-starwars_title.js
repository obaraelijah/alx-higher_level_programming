#!/usr/bin/node

const request = require('request');
const starWarUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(starWarUrl, (_err, _res, body) => {
   movie = JSON.parse(body);
   console.log(movie.title);
});

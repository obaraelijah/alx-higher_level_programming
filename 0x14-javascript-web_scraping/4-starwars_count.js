#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (_err, _res, body) => {
  const data = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < data.results.length; i++) {
    const chars = data.results[i].characters;
    for (let k = 0; k < chars.length; k++) {
      if (chars[k].includes('18')) {
        count = count + 1;
      }
    }
  }
  console.log(count);
});

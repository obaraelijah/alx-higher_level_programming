#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, _res, body) => {
  if (err) console.log(err);
  const dict = {};
  const tasks = JSON.parse(body);
  for  (let i = 0; i < tasks.length; i++) {
    if (!dict[tasks[i].userId]) {
      dict[tasks[i].userId] = 0;
    }
    if (tasks[i].completed === true) {
      dict[tasks[i].userId] += 1;
    }
  }
  console.log(dict);
});

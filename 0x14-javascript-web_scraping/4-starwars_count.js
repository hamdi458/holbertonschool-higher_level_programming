#!/usr/bin/node
const request = require('request');
let s = 0;
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  for (const item in data.results) {
    for (const obj in data.results[item].characters) {
      if (data.results[item].characters[obj].endsWith('/18/')) {
        s++;
      }
    }
  }
  console.log(s);
});

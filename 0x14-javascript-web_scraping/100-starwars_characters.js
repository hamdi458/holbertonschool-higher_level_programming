#!/usr/bin/node
/*  script that prints all characters of a Star Wars movie */
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body).characters;
  data.forEach((chr) => {
    request(chr, function (err1, response, body1) {
      if (!err1) {
        console.log(JSON.parse(body1).name);
      }
    });
  });
});

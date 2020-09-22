#!/usr/bin/node
const request = require('request');
const obj = {};
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  data.forEach((todo) => {
    if (todo.completed === true && obj[todo.userId] === undefined) obj[todo.userId] = 1;
    else if (todo.completed === true) obj[todo.userId] += 1;
  });
  console.log(obj);
});

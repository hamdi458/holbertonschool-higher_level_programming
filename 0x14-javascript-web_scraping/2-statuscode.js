#!/usr/bin/node
const fs = require('request');
fs.get(process.argv[2]).on('response', function (fs) {
  console.log(`code: ${fs.statusCode}`);
});

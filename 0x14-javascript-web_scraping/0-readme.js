#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (err1, data) {
  if (err1) throw err1;
  else console.log(data);
});

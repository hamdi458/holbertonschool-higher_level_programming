#!/usr/bin/node
const fs = require('fs');
const a = fs.readFileSync(process.argv[2], 'utf8', function (err1, data) {
    if (err1) throw err1;
    console.log(data);
  });
const b = fs.readFileSync(process.argv[3],'utf8', function (err2, data) {
    if (err2) throw err2;
    console.log(data);
  });
fs.writeFileSync(process.argv[4], a + b);
#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const pro = fs.createWriteStream(process.argv[3]);
request(process.argv[2]).pipe(pro);

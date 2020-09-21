#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newdict = {};
for (const key in dict) {
  if (!newdict[dict[key]]) {
    newdict[dict[key]] = [key];
  } else {
    newdict[dict[key]].push(key);
  }
}
console.log(newdict);

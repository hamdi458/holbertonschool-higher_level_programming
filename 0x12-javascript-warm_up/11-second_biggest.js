#!/usr/bin/node
const array = [];
if (process.argv.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    array.push(process.argv[i]);
  }
  const intArray = array.map(Number);
  console.log(intArray.sort(function (a, b) { return (b - a); })[1]);
}

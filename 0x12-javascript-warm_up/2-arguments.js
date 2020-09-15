#!/usr/bin/node
const l = process.argv.length;
if (l === 2) {
  console.log('No argument');
} else if (l === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

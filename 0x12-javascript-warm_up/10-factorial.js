#!/usr/bin/node
function fact (nbr) {
  let i;
  let f = 1;
  for (i = 1; i <= nbr; i++) {
    f = f * i;
  }
  return f;
}
console.log(fact(process.argv[2]));

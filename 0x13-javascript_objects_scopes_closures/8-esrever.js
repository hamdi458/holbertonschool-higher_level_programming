#!/usr/bin/node
exports.esrever = function (list) {
  const newarray = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newarray.push(list[i]);
  }
  return newarray;
};

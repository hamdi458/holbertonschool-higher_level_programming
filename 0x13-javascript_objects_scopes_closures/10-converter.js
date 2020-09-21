#!/usr/bin/node
exports.converter = function (base) {
  return Number => Number.toString(base);
};

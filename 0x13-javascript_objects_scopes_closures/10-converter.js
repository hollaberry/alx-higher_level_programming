#!/usr/bin/node
exports.converter = function (base) {
  function change (number) {
    return number.toString(base);
  }
  return change;
};

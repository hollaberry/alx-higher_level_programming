#!/usr/bin/node

let myargs = 0;
exports.logme = function (item) {
  console.log(myargs + ': ' + item);
  myargs++;
};

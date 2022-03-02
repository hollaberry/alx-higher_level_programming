#!/usr/bin/node

let myargs = 0;
exports.logMe = function (item) {
  console.log(myargs + ': ' + item);
  myargs++;
};

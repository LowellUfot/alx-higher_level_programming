#!/usr/bin/node
exports.callMeMoby = function (j, aFunction) {
  for (let i = 0; i < j; i++) {
    aFunction();
  }
};

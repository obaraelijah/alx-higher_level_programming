#!/usr/bin/node

function callMeMoby (n, theFunction) {
  for (let i = 0; i < n; i++) {
    theFunction();
  }
}
module.exports.callMeMoby = callMeMoby;

#!/usr/bin/node

function addMeMaybe(n, theFunction) {
  n++;
  theFunction(n);
}

module.exports.addMeMaybe = addMeMaybe;

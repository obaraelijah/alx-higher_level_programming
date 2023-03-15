#!/usr/bin/nod

exports.esrever = function (list) {
  return list.reduceRight(function (arr, last) {
    return (arr = arr.concat(last));
  }, []);
};

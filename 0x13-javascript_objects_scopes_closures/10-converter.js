#!/usr/bin/node

exports.converter = function (b) {
  return function (val) {
    return val.toString(b);
  };
};

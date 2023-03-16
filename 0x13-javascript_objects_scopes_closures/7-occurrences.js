#!/usr/bin/node

exports.nbOccurences = function (hst, ndl) {
  let c = 0;
  for (let i = 0; i < hst.length; i++) {
    if (Array.isArray(hst) && hst[i] === ndl) {
      c++;
    }
  }
  return (c);
};

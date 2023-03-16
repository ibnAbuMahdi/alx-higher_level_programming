#!/usr/bin/node

const data = require('./101-data');
const newDict = {};
for (const n in data.dict) {
  if (data.dict[n] in newDict) {
    newDict[data.dict[n]].push(n);
  } else {
    newDict[data.dict[n]] = [n];
  }
}
console.log(newDict);

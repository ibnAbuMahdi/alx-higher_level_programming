#!/usr/bin/node

const list = require('./100-data');
const newList = list.list.map((x, i) => i * x);
console.log(list.list);
console.log(newList);

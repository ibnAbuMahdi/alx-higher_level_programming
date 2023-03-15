#!/usr/bin/node

function add (a, b) {
  return (a + b);
}
const args = process.argv;
const num = Number(args[2]);
const num1 = Number(args[3]);
console.log(add(num, num1));

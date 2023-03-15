#!/usr/bin/node

const args = process.argv;
const numb = Number(args[2]);

function fact (num) {
  if (isNaN(num) || num === 0 || num === 1) {
    return (1);
  } else {
    return (num * fact(num - 1));
  }
}

if (isNaN(numb) || numb >= 0) {
  console.log(fact(numb));
}

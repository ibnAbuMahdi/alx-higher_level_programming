#!/usr/bin/node

const args = process.argv;
const num = Number(args[2]);
if (!isNaN(parseFloat(num)) && isFinite(num)) {
  console.log('My number: ' + parseInt(num));
} else {
  console.log('Not a number');
}

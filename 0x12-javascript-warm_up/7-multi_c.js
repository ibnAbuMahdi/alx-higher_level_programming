#!/usr/bin/node

const args = process.argv;
const num = Number(args[2]);
if (!isNaN(parseFloat(num)) && isFinite(num)) {
  for (let i = 0; i < parseInt(num); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}

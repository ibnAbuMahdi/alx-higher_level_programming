#!/usr/bin/node

const args = process.argv;
const num = Number(args[2]);
if (!isNaN(parseFloat(num)) && isFinite(num)) {
  for (let i = 0; i < parseInt(num); i++) {
    for (let j = 0; j < parseInt(num); j++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
} else {
  console.log('Missing size');
}

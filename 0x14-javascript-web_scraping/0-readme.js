#!/usr/bin/node

const proc = require('process');
const fs = require('fs');
const args = proc.argv;
if (args.length === 3) {
  fs.readFile(proc.argv[2], 'utf8', (error, data) => {
    if (error) { console.log(error); } else { console.log(data); }
  });
}

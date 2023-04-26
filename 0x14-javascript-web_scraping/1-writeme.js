#!/usr/bin/node

const proc = require('process');
const fs = require('fs');
const args = proc.argv;
if (args.length === 4) {
  fs.writeFile(proc.argv[2], Buffer.from(proc.argv[3], 'utf-8').toString(), (error) => {
    if (error) { console.log(error); }
  });
}

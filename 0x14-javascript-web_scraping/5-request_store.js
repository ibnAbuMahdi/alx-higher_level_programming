#!/usr/bin/node

const proc = require('process');
const fs = require('fs');
const request = require('request');
const args = proc.argv;
if (args.length === 4) {
  request(args[2]).pipe(fs.createWriteStream(args[3], { flags: 'w', encoding: 'UTF8', mode: 0o666 }));
}

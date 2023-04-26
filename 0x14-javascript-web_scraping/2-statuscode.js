#!/usr/bin/node

const proc = require('process');
const request = require('request');
const args = proc.argv;
if (args.length === 3) {
  request
    .get(proc.argv[2])
    .on('response', (response) => {
      console.log('code:', response.statusCode);
    });
}

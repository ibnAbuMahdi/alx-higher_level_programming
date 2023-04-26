#!/usr/bin/node

const proc = require('process');
const request = require('request');
const args = proc.argv;
if (args.length === 3) {
  request('https://swapi-api.alx-tools.com/api/films/' + args[2], (error, resp, body) => {
    if (error === null && resp.statusCode === 200) { console.log(JSON.parse(body).title); }
  });
}

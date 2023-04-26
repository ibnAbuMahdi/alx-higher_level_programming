#!/usr/bin/node

const proc = require('process');
const request = require('request');
const args = proc.argv;
if (args.length === 3) {
  let count = 0;
  request(args[2], (error, resp, body) => {
    if (error === null && resp.statusCode === 200) {
      const films = JSON.parse(body).results;
      films.forEach((e, i, a) => {
        const chars = e.characters;
        chars.forEach((ele, ind, arr) => {
          if (ele.includes('18')) { count++; }
        });
      });
      console.log(count);
    }
  });
}

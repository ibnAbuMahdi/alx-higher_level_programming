#!/usr/bin/node

const proc = require('process');
const request = require('request');
const args = proc.argv;
if (args.length === 3) {
  request(args[2], (error, resp, body) => {
    if (error === null && resp.statusCode === 200) {
      const todos = JSON.parse(body);
      const obj = {};
      let c = 0;
      todos.forEach((e, i, a) => {
        if (e.userId in obj) { if (e.completed) c++; } else { if (e.completed) c = 1; else c = 0; }
        obj[e.userId] = c;
      });
      console.log(obj);
    }
  });
}

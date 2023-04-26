#!/usr/bin/node

const proc = require('process');
const request = require('request');
const args = proc.argv;
if (args.length === 3) {
  request(args[2], (error, resp, body) => {
    if (error === null && resp.statusCode === 200) {
      const todos = JSON.parse(body);
      const obj = {};
      todos.forEach((e, i, a) => {
        if (e.userId in obj) {
          if (e.completed) obj[e.userId]++;
        } else {
          if (e.completed) obj[e.userId] = 1;
        }
      });
      console.log(obj);
    }
  });
}

#!/usr/bin/node

const request = require('request');
request('https://jsonplaceholder.typicode.com/todos', (error, resp, body) => {
  if (error === null && resp.statusCode === 200) {
    const todos = JSON.parse(body);
    const obj = {};
    let c = 0;
    todos.forEach((e, i, a) => {
      if (e.userId in obj) { if (e.completed) c++; } else { if (e.completed) { c = 1; } else { c = 0; } }
      obj[e.userId] = c;
    });
    console.log(obj);
  }
});

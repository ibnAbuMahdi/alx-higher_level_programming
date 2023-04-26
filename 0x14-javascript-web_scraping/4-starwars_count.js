#!/usr/bin/node

const request = require('request');
let count = 0;
request('https://swapi-api.alx-tools.com/api/films/', (error, resp, body) => {
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

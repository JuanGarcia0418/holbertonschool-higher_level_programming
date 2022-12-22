#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
request(`https://swapi-api.hbtn.io/api/films/${argv[2]}`, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const obtained = JSON.parse(body);
    console.log(`${obtained.title}`);
  }
});

#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + parseInt(process.argv[2]);

request(url, (err, res, body) => {
  if (err) throw err;

  console.log(JSON.parse(body).title);
});

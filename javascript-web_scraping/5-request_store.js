#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];

request(process.argv[2], (err, res, body) => {
  if (err) throw err;
  fs.writeFile(process.argv[3], body, 'utf-8', (err, data) => {
    if (err) throw err;
  });
});

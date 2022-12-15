#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) throw err;
  const users = {};
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      if (users[task.userId]) {
        users[task.userId]++;
      } else {
        users[task.userId] = 1;
      }
    }
  }
  console.log(users);
});

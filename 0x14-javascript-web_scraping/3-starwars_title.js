#!/usr/local/bin/node

// Read the file and print its contents.
const link = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const request = require('request');
request(link, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const jsonDict = JSON.parse(body);
    console.log(jsonDict.title);
  }
});

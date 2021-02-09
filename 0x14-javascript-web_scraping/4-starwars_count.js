#!/usr/bin/node

// Read the file and print its contents.
const link = process.argv[2];
const request = require('request');
let temp = 0;
const name = 'https://swapi-api.hbtn.io/api/people/18/';

request(link, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const jsonDict = JSON.parse(body);

    for (let i = 0; i < jsonDict.results.length; i++) {
      for (let x = 0; x < jsonDict.results[i].characters.length; x++) {
        if (name === jsonDict.results[i].characters[x]) {
          temp++;
        }
      }
    }
    console.log(temp);
  }
});

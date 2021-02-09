#!/usr/bin/node

// Read the file and print its contents.
const link = process.argv[2];
const https = require('https');

https.get(link, function (res) {
  console.log('code: ', res.statusCode); // <======= Here's the status code
});

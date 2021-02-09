#!/usr/local/bin/node

// Read the file and print its contents.
const fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, 'utf8', function (err, data) {
  if (data) {
    console.log(data);
  } else {
    console.log(err);
  }
});

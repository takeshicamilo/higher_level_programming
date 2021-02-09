#!/usr/bin/node

// Read the file and print its contents.
const fs = require('fs');
const filename = process.argv[2];
const text = process.argv[3];
fs.writeFile(filename, text, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
});

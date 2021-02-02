#!/usr/local/bin/node
// xddd

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let y = 0; y < process.argv[2]; y++) {
    console.log('X'.repeat(process.argv[2]));
  }
}

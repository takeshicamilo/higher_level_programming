#!/usr/bin/node
// xddd

const c = 'C is fun';

if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < process.argv[2]; x++) {
    console.log(c);
  }
}

#!/usr/local/node
// xddd

if (process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let y = 0; y < process.argv[2]; y++) {
    console.log('X'.repeat(process.argv[2]));
  }
}

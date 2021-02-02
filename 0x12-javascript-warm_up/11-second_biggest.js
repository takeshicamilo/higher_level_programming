#!/usr/bin/node
// xddd

let y = 0;
let temp = 0;
for (let x = 0; x < process.argv.length; x++) {
  if (y < parseInt(process.argv[x])) {
    y = parseInt(process.argv[x]);
  }
}
for (let z = 0; z < process.argv.length; z++) {
  if (temp < parseInt(process.argv[z])) {
    if (parseInt(process.argv[z]) !== y) {
      temp = parseInt(process.argv[z]);
    }
  }
}
console.log(temp);

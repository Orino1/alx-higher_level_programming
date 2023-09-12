#!/usr/bin/node
const array = [];
let i = 2;
if (process.argv.length < 4) {
  console.log(0);
} else {
  while (i < process.argv.length) {
    array.push(parseInt(process.argv[i]));
    i++;
  }
  array.sort((a, b) => b - a);
  console.log(array[1]);
}

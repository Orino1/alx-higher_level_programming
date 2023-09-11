#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let line = '';
    for (let y = 0; y < size; y++) {
      line += 'X';
    }
    console.log(line);
  }
}

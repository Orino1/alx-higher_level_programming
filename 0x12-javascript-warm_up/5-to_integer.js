#!/usr/bin/node
try {
  if (process.argv[2] === undefined) {
    throw new Error();
  }
  const mynumber = parseInt(process.argv[2]);
  if (isNaN(mynumber)) {
    throw new Error();
  }
  console.log('My number: ' + mynumber);
} catch {
  console.log('Not a number');
}

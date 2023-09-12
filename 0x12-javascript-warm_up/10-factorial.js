#!/usr/bin/node
function factorial (number) {
  if (number <= 1) {
    return 1;
  }
  return number * factorial(number - 1);
}
const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log(1);
} else {
  const facto = factorial(number);
  console.log(facto);
}

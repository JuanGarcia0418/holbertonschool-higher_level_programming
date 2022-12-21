#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  let num = 0;
  while (num < process.argv[2]) {
    console.log('C is fun');
    num++;
  }
}

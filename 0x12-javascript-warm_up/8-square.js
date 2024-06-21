#!/usr/bin/node
/* prscript that prints a square */

const x = 'X';
if (!isNaN(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    let square = '';
    for (let j = 0; j < process.argv[2]; j++) {
      square += x;
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}

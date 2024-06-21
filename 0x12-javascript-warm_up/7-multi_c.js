#!/usr/bin/node
/* print first argument converted in integer */

const x = 'C is fun';

if (! isNaN(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(x);
  }
} else {
  console.log('Missing number of occurrences');
}

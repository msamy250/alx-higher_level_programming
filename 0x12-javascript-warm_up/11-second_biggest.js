#!/usr/bin/node
/* searches the second biggest integer */



if (process.argv.length > 2) {
  const list = process.argv.sort()
  console.log(list.reverse()[1]);
} else {
  console.log(0);
}
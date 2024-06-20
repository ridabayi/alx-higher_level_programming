#!/usr/bin/node

const arg = process.argv[2];

if (arg === undefined) {
  console.log('No Argument');
} else {
  console.log(arg);
}

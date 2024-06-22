#!/usr/bin/node

// Function that adds two numbers
function add (a, b) {
  return a + b;
}

// Get command-line arguments
const args = process.argv.slice(2);

// Parse the arguments to integers
const num1 = parseInt(args[0]);
const num2 = parseInt(args[1]);

// Check if the arguments are valid numbers
if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  // Call the add function and print the result
  console.log(add(num1, num2));
}

#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Use filter to create a new array with elements that match searchElement
  const occurrences = list.filter(element => element === searchElement);
  
  // The length of the occurrences array gives the number of matches
  return occurrences.length;
};

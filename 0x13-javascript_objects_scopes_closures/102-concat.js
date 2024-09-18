#!/usr/bin/node

// const { rejects } = require('assert');
const fs = require('fs');
// const path = require('path');

// Check if the correct number of arguments is provided
if (process.argv.length !== 5) {
  console.error(
    'Usage: ./102-concat.js <source_file1> ' +
        '<source_file2> <destination_file>'
  );
  process.exit(1);
}

// Get file paths from command-line arguments
const [sf1, sf2, df1] = process.argv.slice(2);

try {
  // REad contents of the source files
  const content1 = fs.readFileSync(sf1, 'utf-8');
  const content2 = fs.readFileSync(sf2, 'utf-8');

  // Concatenate the contents with a newline in between
  const combinedContent = content1 + content2;

  // Write the combined contents to the destination
  fs.writeFileSync(df1, combinedContent, 'utf-8');
} catch (err) {
  console.error('Error:', err.message);
  process.exit(1);
}

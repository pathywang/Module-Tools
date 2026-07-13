const fs = require("fs");

const args = process.argv.slice(2);

const numberLines = args[0] === "-n";

const files = numberLines ? args.slice(1) : args;

let lineNumber = 1;

for (const file of files) {
  const content = fs.readFileSync(file, "utf8");

  const lines = content.split("\n");

  for (const line of lines) {
    if (numberLines) {
      console.log(`${String(lineNumber).padStart(6)}\t${line}`);
      lineNumber++;
    } else {
      console.log(line);
    }
  }
}
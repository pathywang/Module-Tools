const fs = require("fs");

const args = process.argv.slice(2);

const numberLines = args[0] === "-n";

const filename = numberLines ? args[1] : args[0];

const content = fs.readFileSync(filename, "utf8");

const lines = content.split("\n");

if (numberLines) {
  lines.forEach((line, index) => {
    console.log(`${String(index + 1).padStart(6)}\t${line}`);
  });
} else {
  process.stdout.write(content);
}
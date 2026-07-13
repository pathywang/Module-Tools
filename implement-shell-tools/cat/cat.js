const fs = require("fs");

const files = process.argv.slice(2);

for (const file of files) {
  const content = fs.readFileSync(file, "utf8");
  process.stdout.write(content);
}
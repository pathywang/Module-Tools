const fs = require("fs");

const args = process.argv.slice(2);

let countLines = false;
let countWords = false;
let countBytes = false;
let files = [];

for (const arg of args) {
    if (arg === "-l") {
        countLines = true;
    } else if (arg === "-w") {
        countWords = true;
    } else if (arg === "-c") {
        countBytes = true;
    } else {
        files.push(arg);
    }
}

// If no flags are given, wc shows all three
if (!countLines && !countWords && !countBytes) {
    countLines = true;
    countWords = true;
    countBytes = true;
}

function countFile(filename) {
    const content = fs.readFileSync(filename, "utf8");

    const lines = content.split("\n").length - 1;
    const words = content.trim() === "" ? 0 : content.trim().split(/\s+/).length;
    const bytes = Buffer.byteLength(content);

    let output = [];

    if (countLines) {
        output.push(lines);
    }

    if (countWords) {
        output.push(words);
    }

    if (countBytes) {
        output.push(bytes);
    }

    output.push(filename);

    console.log(output.join(" "));
}

for (const file of files) {
    countFile(file);
}
import sys

args = sys.argv[1:]

count_lines = False
count_words = False
count_bytes = False
files = []

for arg in args:
    if arg == "-l":
        count_lines = True
    elif arg == "-w":
        count_words = True
    elif arg == "-c":
        count_bytes = True
    else:
        files.append(arg)

# If no flags are given, wc shows all three
if not count_lines and not count_words and not count_bytes:
    count_lines = True
    count_words = True
    count_bytes = True


def count_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

        lines = content.count("\n")

        words = 0 if content.strip() == "" else len(content.split())

        # UTF-8 bytes, same idea as Buffer.byteLength()
        bytes_count = len(content.encode("utf-8"))

        output = []

        if count_lines:
            output.append(str(lines))

        if count_words:
            output.append(str(words))

        if count_bytes:
            output.append(str(bytes_count))

        output.append(filename)

        print(" ".join(output))

        return {
            "lines": lines,
            "words": words,
            "bytes": bytes_count
        }

    except Exception as err:
        print(f"wc: {filename}: {err}")
        return None


total_lines = 0
total_words = 0
total_bytes = 0

for file in files:
    counts = count_file(file)

    if counts:
        total_lines += counts["lines"]
        total_words += counts["words"]
        total_bytes += counts["bytes"]


if len(files) > 1:
    output = []

    if count_lines:
        output.append(str(total_lines))

    if count_words:
        output.append(str(total_words))

    if count_bytes:
        output.append(str(total_bytes))

    output.append("total")

    print(" ".join(output))
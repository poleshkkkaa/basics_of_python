import os

input_file = "input.txt"
output_file = "output.txt"

if not os.path.exists(input_file):
    print("файл input.txt не знайдено")
else:
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    if text.strip() == "":
        print("файл порожній")
    else:
        words = text.split()
        word_count = len(words)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(str(word_count))

        print(f"результати записано у файл {output_file}")

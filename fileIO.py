from collections import Counter
import re

with open('sample.txt') as f:
    contents = f.read()

words = re.findall(r'\b\w+\b', contents.lower())
top_10 = Counter(words).most_common(10)


line_count = 0
word_count = 0
char_count = 0
with open('sample.txt') as f:
    for line in f:
        line_count += 1
        words = line.split()
        word_count += len(words)
        char_count += sum(1 for char in line if not char.isspace())

print(line_count)
print(word_count)
print(char_count)



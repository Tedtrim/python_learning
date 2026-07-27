from collections import Counter
import re

with open('sample.txt') as f:
    contents = f.read()

print(len(contents))

words = re.findall(r'\b\w+\b', contents.lower())

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

top = sorted(counts.items(), key=lambda item: item[1], reverse=True)
top_10 = top[0:10]

for word, n in top_10:
    print(f'Word: {word}  Count: {n}')


line_count = 0
word_count = 0
char_count = 0

for line in contents:
    line_count += 1
    words = line.split()
    word_count += len(words)
    char_count += sum(1 for char in line if not char.isspace())

print(line_count)
print(word_count)
print(char_count)





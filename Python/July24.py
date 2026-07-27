squares = [x ** 2 for x in range(10)]
total = sum(squares)
first_three = squares[0:4]

print(squares)
print(total)
print(first_three)

import string

counts = {}
top_10 = {}

with open('sample.txt') as f:
    for line in f:
        for word in line.split():
            word = word.strip(string.punctuation).lower()
            if word not in counts:
                counts[word] = 0
            counts[word] += 1

ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
top_10 = ranked[:10]


print(top_10)
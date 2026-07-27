from functools import reduce

lambda x: x ** 3

def is_odd(n):
    return n % 2 == 1

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds = filter(lambda n: n % 2 == 1, nums)
odds2 = [n for n in nums if n % 2 == 1]

animals = [('spider', 8), ('dog', 4), ('bird', 2), ('ant', 6)]
leg_count_asc = sorted(animals, key=lambda animal: animal[1])

scores = {'alice': 90, 'bob': 78, 'carol': 85}
highest = sorted(scores.items(), key=lambda item: item[1], reverse=True)

nums1 = [2, 3, 4, 5]
r = reduce(lambda x, y: x * y, nums1)
print(r)


words = ['cat', 'elephant', 'fox', 'butterfly', 'ant']
result = max(words, key=lambda word: len(word))
print(result)

result2 = max(words, key=len)

nums = [42, 7, 19, 3, 88, 56]
sort_descending = sorted(nums, reverse=True)
print(sort_descending)

fruits = ['banana', 'fig', 'apple', 'kiwi', 'pomegranate']
result3 = sorted(fruits, key=len)
print(result3)
shortest_fruit = min(fruits, key=len)#
print(shortest_fruit)

list1 = [(-5, 'a'), (3, 'b'), (-8, 'c'), (1, 'd')]
asc_abs = sorted(list1, key=lambda item: abs(item[0]))
print(asc_abs)

students = [('alice', 88), ('bob', 45), ('carol', 73)]
highest_student = max(students, key=lambda student: student[1])
print(highest_student)

words1 = ['Banana', 'apple', 'Cherry', 'date']
sorted_words = sorted(words1, key=str.lower)
print(sorted)

records = [
    {'name': 'alice', 'score': 88, 'year': 2},
    {'name': 'bob',   'score': 45, 'year': 1},
    {'name': 'carol', 'score': 73, 'year': 2},
    {'name': 'dave',  'score': 91, 'year': 3},
    {'name': 'zara', 'score': 88, 'year': 1},
]

score_desc = sorted(records, key=lambda record: record['score'], reverse=True)
top_names = [student['name'] for student in score_desc]
print(top_names)

filter_records = [record for record in records if record['year'] == 2]
max_year2 = max(filter_records, key=lambda record: record['score'])
print(max_year2)

sorted_by_score = sorted(records, key=lambda r: (-r['score'], r['name']))
print(sorted_by_score)

points = [(3, 4), (1, 1), (5, 12), (0, 0), (8, 6)]
dist_from_origin = sorted(points, key=lambda point: (point[0]**2 + point[1]**2) ** 0.5)
print(dist_from_origin)

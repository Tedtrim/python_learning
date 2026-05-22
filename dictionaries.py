spending = {
    'groceries': 85.60,
    'transport': 20.50,
    'coffee': 4.50,
    'rent': 800.00,
    'utilities': 90.00,
    'eating_out': 65.00,
}

big_buys = {cat: f'£{amt:.2f}' for cat, amt in spending.items() if amt >= 20}

print(big_buys)

squares_of_evens = [x*x for x in range(20) if x % 2 == 0]
print(squares_of_evens)

cubes = [x*x*x for x in range(11)]
print(cubes)

words1 = ['Hello', 'World', 'Python', 'Java']
lowercase = [word.lower() for word in words1]
print(lowercase)

multiples_of_three = [x for x in range(30) if x % 3 == 0]
print(multiples_of_three)

nums = [-2, -1, 0, 3, 5, -7, 8]
comp1 = [x if x > 0 else 0 for x in nums]
print(comp1)

words2 = ['apple', 'banana', 'cherry']
comp2 = {word: len(word) for word in words2}
print(comp2)

scores = {'alice': 88, 'bob': 45, 'carol': 73, 'dave': 39, 'eve': 91}
students_passed = {student: score for student, score in scores.items() if score >= 50} 
print(students_passed)

names = ['alice', 'bob', 'carol']
ages = [21, 22, 20]
comp3 = {name: age for name, age in zip(names, ages)}
print(comp3)

records = [{'name': 'alice', 'score': 88}, {'name': 'bob', 'score': 45}, {'name': 'carol', 'score': 73}]
comp4 = [student['name'] for student in records if student['score'] >= 50]
print(comp4)



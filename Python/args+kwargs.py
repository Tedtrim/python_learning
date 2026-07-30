import math

def multiply_all(*args):
    return math.prod(args)

print(multiply_all(2, 5, 6))

def baz(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

print(baz(Name="Ted", Age=19, City="London"))

def greet(name, *others):
    print(name)
    print(others)

greet("Alice", "Bob", "Carol")
greet("Alice")

def show(**options):
    print(options)
    print(len(options))
    print(options.get("size", 0))

show(colour="red")

def average(*numbers):
    if not numbers:
        raise ValueError("average() requires at least one number")
    
    return sum(numbers) / len(numbers)

  
def f(a, *args, **kwargs):
    print(a, args, kwargs)

f(1)
f(1, 2, 3)
f(1, 2, x=3, y=4)

def tally(**scores):
    highest_score = max(scores.items(), key=lambda score: score[1])
    return highest_score[0]


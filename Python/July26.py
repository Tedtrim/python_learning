nums = [5, 6, 1, 2, 8, 4, 12]

print(nums[2:6])
print(nums[1:-2])
print(nums[::-1])
print(nums[4:-5])
print(nums[1:5:2])
print(nums[1:4:1])
print(nums[0:6:3])
print(nums[0:3:1])
print(nums[3:0:1])

def square_func(n):
    for x in range(n):
        yield x**2

def stripped_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
    
print(stripped_lines('sample.txt'))

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b



def gen(): yield 1

print(gen())

def logged(foo):
    def wrapper(*args, **kwargs):
        return foo()
    return wrapper
 
@logged
def foo(*args, **kwargs):
    print(*args, **kwargs)
    

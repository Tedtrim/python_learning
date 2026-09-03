funcs = [lambda x=i: x for i in range(3)]
print([f() for f in funcs]) 


def squares(n):
    print("starting")
    for i in range(n):
        yield i * i

g = squares(3)
print("created")
print(next(g))

def beforeafter(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args,**kwargs)
        print("after")
        return result
    return wrapper

@beforeafter
def foo():
    print("Hello Claude")



funcs = []
for i in range(3):
    funcs.append(lambda: i)
print([f() for f in funcs])


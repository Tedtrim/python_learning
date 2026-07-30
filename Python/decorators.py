
def add_sprinkles(func):
    def wrapper():
        func()
        print("*Added sprinkles*")
    return wrapper

@add_sprinkles
def ice_cream():
    print("I have an ice cream!")

ice_cream()


def shout(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@shout
def greet():
    return "Hello"

@shout
def greet_person(name):
    return f"hello {name}"

print(greet_person("Ted"))
print(greet())


def hello():
    print("Hello, World!")

hello()

def sum(num1 = 0, num2 = 7):
    if(type(num1) is not int or type(num2) is not int):
        raise ValueError("Both arguments must be integers")
    return num1 + num2

total = sum(44)
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items(78, "Hello", [1, 2, 3], {"name": "Alice"})
    

def named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

named_items(name="Bob", age=30, city="New York")
def add_one(num):
    if num >= 9:
        return num + 1
    total = num + 1
    print(total)
    return add_one(total)

add_one(2)

# Recursion is a programming technique where a function calls itself in order to solve a problem. It typically involves a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems. In the example above, the function `add_one` calls itself until the input number reaches 9 or greater, at which point it returns the final result.

mynew_total = add_one(5)
print(mynew_total)
squared = lambda num : num * num

print(squared(5))

addTwo = lambda num : num + 2

print(addTwo(2))

sum = lambda a, b : a + b

print(sum(3, 4))

def funcBuilder(x):
    return lambda num: num + x


print(funcBuilder(5)(10))


####################### Higher order functions #######################



numbers = [2, 4, 6, 8, 11]

squaredNumbers = map(lambda num: num * num, numbers)

print(list(squaredNumbers))

lambda num: num % 2 != 0

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

###################################

from functools import reduce

# lambda acc, curr: acc + curr

numbers = [2, 4, 6, 8, 11]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

# The third argument is the starting value in the above

print(total)


names = ["Ayinde Abdulrahman", "Ololade Olayiwola", "Oluwanisola Abeke"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
# if the third argument is not provided, the first element of the list will be used as the starting value
print(char_count)
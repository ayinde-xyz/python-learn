greeting = "hello world"
print(greeting)

# To start the python terminal, run the command "python" in your command line interface.

# You can run divisions, addition, subtraction, and multiplication in the python terminal below

# >>> 2 * 2
# 4
# >>> 24 / 5
# 4.8
# >>> 330 // 7
# 47
# >>> 330 % 5
# 0
# >>> 

# >>> meaning = 42
# >>> meaning += 1
# >>> meaning

# >>> meaning *= 10
# >>> meaning 
# 430 
# >>> meaning /= 12.3
# >>> meaning 
# 34.959349593495936
# >>> meaning = round(meaning)
# >>> meaning


# >>> x = True
# >>> y = False
# >>> z= True
# >>> not x
# False
# >>> not y
# True
# >>> x and y
# False
# >>> x and z
# True

# For NOT operator, it will return the opposite of the value. So if the value is True, it will return False and if the value is False, it will return True. 

# For AND operator, it will return True if both values are True. If either value is False, it will return False.

# For OR operator, it will return True if at least one value is True. If both values are False, it will return False.

# If and Else Statements

# meaning = 8

# if meaning > 40:
#     print("The meaning of life is greater than 40.")
# else:
#     print("The meaning of life is less than or equal to 40.")

 # Ternary operators
    # print("The meaning of life is greater than 40.") if meaning > 40 else print("The meaning of life is less than or equal to 40.")

#  Arithmetic Operators
#  

pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)

# Concatination
fullname = "John" + " " + "Doe"
print(fullname)

#  Casting a member to a string

statement = "My favourite pizza is " + str(pizza)
print(statement)

# Multiple lines of code can be written in the same line by using a semicolon
multiline = '''
Hey there,

This is a multiline string,
It can be used to write multiple lines of text without using the newline character.
'''

# print(multiline)
# print(multiline.title())
print(multiline.replace("multiline", "multi-line"))


# Escaping special characters

character = "I\"m back at work! \tHey! How are you doing? \nI hope you are doing well."
print(character)

print(len(multiline))
multiline = "                  " +  multiline


print(len(multiline.strip()))
print(len(multiline.rstrip()))
print(len(multiline.lstrip()))


# Build a men
title = "menu".upper()
print(title.center(20, "*"))
print("Coffee".ljust(20, ".") + " $2.50".rjust(10))


# The above string methods is used to justify either right or left or center the string. The first argument is the width of the string and the second argument is the fill character. If the second argument is not provided, it will use a space as the fill character.


# String index values
name = "AbdurRahman"
print(name[0])
print(name[1:-1])
print(name)

myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Float value type
gpa = 4.99
y = float(gpa)
print(type(y))


# Complex type

comp_value = 2 + 3j
print(comp_value.real)
print(comp_value.imag)

print(abs(gpa))
print(abs(gpa * -1))


print(round(gpa))
print(round(gpa, 1))

# the round function rounds a float to the nearest integer. If the second argument is provided, it will round the float to the specified number of decimal places.

import math

print(math.pi)

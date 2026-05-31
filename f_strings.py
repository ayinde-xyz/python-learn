persons = "Olajide"
coins = 10

message = "\n %s has %s coins left." % (persons, coins)
print(message)

message = "\n {1} has {0} coins left.".format(coins, persons)
print(message)

player = {"persons": "Ayinde", "coins": 5}
message = "\n {persons} has {coins} coins left.".format(**player)
print(message)



# f-strings (formatted string literals) are a more concise and readable way to format strings in Python. They allow you to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and their values are inserted into the string.

message = f"\n {persons.lower()} has {coins} coins left."
print(message)

num = 10
print(f"\n2.25 multiplied by {num} is {2.25 * num:.2f}.")

for num in range(1, 6):
    print(f"{num} squared is {num ** 2}.")
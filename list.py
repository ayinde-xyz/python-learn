users = ["Daniel", "Sophie", "John", "Emily"]

data = [1, True, "Hello", 3.14]

print("Daniel" in users)

print(users.index("Sophie"))

print(len(users))

users.append("Michael")
print(users)


users += ["Jason"]
print(users)

users.extend(["Jason", "Sarah"])

users.insert(0, "Bob")

users[2:2] = ["Alice", "Tom"]
print(users)

users[1:3] = ["Charlie", "David"]
print(users)

users.remove("Emily")
print(users)

print(users.pop())

del users[0]
print(users)

data.clear()
print(data)


users.sort()
print(users)

users[1:2] = ["dave"]
users.sort()
print(users)

users.sort(key=str.lower, reverse=True)
print(users)

nums = [5, 2, 9, 1, 3]
nums.reverse()
print(nums)

print(sorted(nums, reverse=True))
# The above does not modify the original list

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(nums)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

mylist = list(["Kayode", 43, True])


# Tuples
# Tuples are immutable, meaning they cannot be modified after creation

mytuple = tuple(("Dave", 42, True))
anothertuple = ("Alice", 30, False)

print(type(mytuple))
print(type(anothertuple))

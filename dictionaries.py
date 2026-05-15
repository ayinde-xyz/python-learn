# Dictionaries

band = {
    "name": "The Beatles",
    "members": ["John", "Paul", "George", "Ringo"],
    "formed": 1960
}

band2 = dict(vocals = "Plant", guitar="Page")


print(type(band))
print(type(band2))
print(len(band))

# Access items

print(band["members"])
print(band.get("formed"))
print(band.keys())
print(band.values())
print(band.items())

# Change values

band["formed"] = 2003
band.update({"name": "Beatles"})
print(band)


# Remove items

# print(band.pop("members"))
# print(band)

band["location"] = "London"

print(band.popitem())
print(band)

# Delete and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

band2 = band
#  The above is a bad copy.

print(band2)
print(band)

band3 = dict(band)
print(band3)

# Nested dictionaries

member1 = { "name": "John", "instrument": "vocals" }
member2 ={"name": "james", "instrument": "guitar" }

band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])

# Sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums2))


# Sets are unordered and do not allow duplicates

nums ={1, 2, 3, 4, 4, 4}
print(nums)

# True is a duplicate of 1 and False is a duplicate of 0

nums = {1, True, False, 0, 3, 4}
print(nums)

# Check if a value is in a set
print(2 in nums)

nums.add(8)
print(nums)

morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# merge 2 sets

one ={1, 2 ,3}
two = {2, 3, 7}

# mynewset = one.union(two)
# print(mynewset)

# one.intersection_update(two)
# print(one)
one.symmetric_difference_update(two)
print(one)


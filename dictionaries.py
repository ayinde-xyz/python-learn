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

print(band.pop("members"))
print(band)

band["location"] = "London"

print(band.popitem())
print(band)
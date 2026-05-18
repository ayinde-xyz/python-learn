value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1


# while value <= 10:
#     value += 1
#     if value == 4:
#         continue
#         print(value)
#     else: 
#         print("value is now complete")
# continue statement will skip the rest of the code in the loop and move to the next iteration, while break statement will exit the loop completely.

names = ["Alice", "Bob", "Chase", "Crawford"]

# for name in names:
#     if name == "Chase":
#         continue
#     print(name)

# for name in names:
#         if name == "Crawford":
#             continue
#         print(name)

# for x in range(10):
#     if x % 2 == 0: 
#         continue 
#     print(x)

# for x in range(0, 100, 10):
#     print(x)
# else: 
#     print("Loop is complete")

actions = ["run", "jump", "swim", "dance"]


for name in names:
    for action in actions:
        print(f"{name} likes to {action}")

        

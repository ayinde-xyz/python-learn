name = "Dave"
count = 1

def another_greet():
    global count
    count += 1
    print(count)
    color = "blue"


    def greet(firstname):
        nonlocal color
        color = "purple"
        print(color)
        print(firstname)
        print(f"The color is {color}.")
        print(f"Hello, {name}!")

    greet("Ayobami")

another_greet()
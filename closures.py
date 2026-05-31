def parent_function(person: str, coins: int = 3):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1
        if coins > 1:
            print(f"{person} has {coins} coins left.")
        elif coins == 1:
            print(f"{person} has {coins} coin left.")
        else:
            print(f"{person} has no coins left. Game over.")

    return play_game
tommy = parent_function("Tommy", 5)
jenny = parent_function("Jenny", 3)

tommy()
tommy()
jenny()

tommy()

# Closures are functions that can access variables from their enclosing scope, even after the outer function has finished executing. In this example, the play_game function is a closure that retains access to the coins variable from the parent_function, allowing it to modify and access the coins variable each time it is called.
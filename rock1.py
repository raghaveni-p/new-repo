def winner(player, computer):
    rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if player not in rules or computer not in rules:
        raise KeyError("Invalid input")

    if player == computer:
        return "draw"
    elif rules[player] == computer:
        return "player"
    else:
        return "computer"


if _name_ == "_main_":
    import random
    choices = ["rock", "paper", "scissors"]

    player = input("Enter rock, paper, or scissors: ").lower()
    computer = random.choice(choices)

    print("Computer chose:", computer)
    print("Result:", winner(player, computer))

import random
while True:
    choices = ["R", "P", "S"]
    player = None
    CPU = random.choice(choices)
    while player not in choices:
        player = input("R, P or S : ").lower()

    if player == CPU:
        print("CPU : ", CPU)
        print("Player : ", player)
        print("Tie !")
    elif CPU == "R":
        if player == "S":
            print("CPU : ", CPU)
            print("Player : ", player)
            print("You Lose")
        if player == "P":
            print("CPU : ", CPU)
            print("Player : ", player)
            print("You Win")
    elif CPU == "P":
        if player == "S":
            print("CPU : ", CPU)
            print("Player : ", player)
            print("You Win")
        if player == "R":
            print("CPU : ", CPU)
            print("Player : ", player)
            print("You Lose")
    elif CPU == "S":
        if player == "R":
            print("CPU : ", CPU)
            print("Player : ", player)
            print("You Win")
        if player == "P":
            print("CPU : ", CPU)
            print("Player : ", player)
            print("You Lose")

    play_again = input("Do you want to play again (Yes/No) : ").lower()

    if play_again != "yes":
        break
print("Bye")
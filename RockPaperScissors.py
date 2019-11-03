def game():
    p1 = input("choose rock paper or scissors for player1: ")
    p2 = input("choose rock paper or scissors for player2: ")
    if p1 == p2:
        print("tie")

    elif p1 == "rock":
        if p2 == "scissors":
            print("player1 win")
        else:
            print("player2 win")

    elif p1 == "paper":
        if p2 == "rock":
            print("player1 win")
        else:
            print("player2 win")

    elif p1 == "scissors":
        if p2 == "paper":
            print("player1 win")
        else:
            print("player2 win")
    else:
        print("Invalid input")

n = 0
while(n != 1):
    game()
    n = int(input("press 1 to quit: "))
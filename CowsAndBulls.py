import random


def compare_num(number, user_guess):
    cows_buls = [0, 0]
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cows_buls[0] += 1
        else:
            cows_buls[1] += 1
    return cows_buls



number = str(random.randint(0, 9999))
guesses = 0
user_guess = ""

while True:
    while len(user_guess) != 4:
        user_guess = input("give me your guess ")
    if user_guess == "exit":
        print(guesses)
        break
    guesses += 1
    cows = compare_num(number, user_guess)
    if cows[0] == 4:
        print("you win, with " + str(guesses) + " guesses")
        break
    else:
        print("cows " + str(cows[0]) + " bulls " + str(cows[1]))
    user_guess = ""

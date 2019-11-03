import random

number = random.randint(1,9)
guess = 0
count = 0

while guess != "exit" and guess != number:
    guess = input("What's your guess? ")
    if guess == "exit":
        break

    guess = int(guess)
    count += 1
    if guess > number:
        print("too high")
    elif guess < number:
        print("too low")
    else:
        print("got it and took you", count, "tries")

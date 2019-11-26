import random


def CreatePassword(len):
    password = ""
    for i in range(len):
        a = random.randint (33, 126)
        password += chr(a)
    print(password)


len = int(input("How many characters in your password? "))
CreatePassword(len)



def sp(x):
    s = " "
    r = x.split(" ")
    print(s.join(r[: : -1]))


test = input("Enter a sentence: ")
sp(test)
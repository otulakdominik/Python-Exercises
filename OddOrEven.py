num = int(input("Enter number to check: "))
check = int(input("Enter a number to divide by: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is a even")
else:
    print(num, "is an odd")

if num % check == 0:
    print(num, "is divides by", check)
else:
    print(num, "does not divide by", check)

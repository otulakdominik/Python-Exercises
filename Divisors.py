num = int(input("Enter your number: "))

divisorList = []

for i in range(2, num):
    if num % i == 0:
        divisorList.append(i)

print(divisorList)

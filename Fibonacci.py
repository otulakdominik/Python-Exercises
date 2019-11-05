def fibo(n):
    a=1
    b=0
    c=0
    for i in range(n):
        print(a)
        c = b + a
        b = a
        a = c

n = int(input("how many fibonnaci numbers to generate: "))
fibo(n)
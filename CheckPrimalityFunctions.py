def is_prime(n):
    if n>1:
        for i in range(2, n-1):
            if n%i == 0:
                print("not prime")
                break
        else:
            print("prime")


num = int(input('Insert a number: '))

is_prime(num)
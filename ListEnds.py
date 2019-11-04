a = [5, 10, 15, 20, 25]

def first_last(a):
    return a[::len(a)-1]

print(first_last(a))
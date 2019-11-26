def dupl1(t):
    a = []
    for i in t:
        if i not in a:
            a.append(i)
    return a


def dupl2(t):
    return list(set(t))


t = [1,2,1,3,3,4,5,6,3]
print(dupl1(t))
print(dupl2(t))
import random

a = random.sample(range(1, 30), random.randint(6,18))
b = random.sample(range(1, 30), random.randint(6,18))

print(set(a) & set(b))
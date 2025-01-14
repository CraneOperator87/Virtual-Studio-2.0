import random

tall = []

tall.append(17)
tall.append(42)
tall.append(81)

for i in range(1,1001):
    n = random.randint(1,100)
    tall.append(n)

tall.sort()
print(tall)
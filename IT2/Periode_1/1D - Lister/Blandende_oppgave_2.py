import random

tall = []
for i in range(1,51):
    tall.append(random.randint(1,100))

tallpartall = []
talloddetall = []

for num in tall:
    if num % 2 == 0:
        tallpartall.append(num)
    else:
        talloddetall.append(num)

print(" ")

tall.sort()
print(f"Liste med tilfeldige tall (1 - 100): {tall}\n")

tallpartall.sort()
print(f"Liste med partall: {tallpartall}\n")

talloddetall.sort()
print(f"Liste med oddetallene: {talloddetall}\n")

synkende = sorted(tall, reverse=True)
print(f"Her er lista med 100 tilfeldige tall i synkende rekkefølge: {synkende}\n")


print("\n\n\n\033[91mprogrammslutt\033[0m\n")
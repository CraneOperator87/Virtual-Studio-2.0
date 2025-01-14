import random
while True:
    try:
        antall = int(input("\nHvor stor vil du ha en liste med tilfeldige tall?: "))

        break
    except ValueError:
        print("\nDu må skrive inn en gyldig heltall!")

tall = []

for n in range(1,antall + 1):
    m = random.randint(1,100)
    tall.append(m)

tall.sort()

if antall % 2 == 0:
    median = antall // 2
    mediantallet = (tall[median - 1] + tall[median]) / 2
    print(f"\nDitt tilfeldiglagd liste med 25 tall, fra 1 til 100:\n")
    print(f"{tall}\n")
    print(f"Medianen i listen: {mediantallet:.2f}\n")
else:
    median = antall // 2
    mediantallet = tall[median]
    print(f"\nDitt tilfeldiglagd liste med 25 tall, fra 1 til 100:\n")
    print(f"{tall}\n")
    print(f"Medianen i listen: {mediantallet}\n")

print("\n\n\n\033[91mprogrammslutt\033[0m\n")


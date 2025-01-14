tall = [5, 2, 4, 3, 1, 6, 9, 8, 7, 10]

tall.sort(reverse=True)

indeks_7 = tall.index(7)
tall.pop(indeks_7)

indeks_9 = tall.index(9)
tall.pop(indeks_9)

tall.remove(2)

tall.append(7)
tall.append(9)
tall.insert(1, 2)

tall.sort(reverse=False)

print(tall)


print("\n\n\n\033[91mprogrammslutt\033[0m\n")
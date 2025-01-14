tall = [0, 1, 2, 0, 0, 3, 4, 5, 0, 0, 6, 0, 7, 0, 8, 0, 0, 0, 9, 10]

while 0 in tall:
    fjernindeks = tall.index(0)
    tall.pop(fjernindeks)

print(tall)
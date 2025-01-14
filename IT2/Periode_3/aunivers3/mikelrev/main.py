filename = "C:/Users/krada/OneDrive/Documents/Github/Virtual-Studio/IT2/Periode_3/aunivers3/mikelrev/MikkelRev.txt"

with open(filename, encoding="utf-8") as data:
    for line in data:
        print(line.rstrip())


file = "./periode_3/aunivers3/rektangler/rektangler.txt"

class Rektangel:
    def __init__(self, lengde, bredde):
        self.lengde = lengde
        self.bredde = bredde

    def areal(self):
        return self.lengde * self.bredde

rektangler = []

with open(file) as f:
    for line in f:
        s = line.rstrip().split(",")
        lengde = int(s[0])
        bredde = int(s[1])

        rektangler.append(Rektangel(lengde, bredde))

for rektangel in rektangler:
    print(rektangel.areal())


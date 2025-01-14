class Rektangel:
    def __init__(self, lengde, bredde):
        self.lengde = lengde
        self.bredde = bredde

    def areal(self):
        return self.lengde * self.bredde

filnavn = "rektangler.txt"
rektangler = []

with open(filnavn, "r", encoding="utf-8") as data:
    for linje in data:
        sidekanter = linje.rstrip().split(",")

        lengde = int(sidekanter[0])
        bredde = int(sidekanter[1])

        rektangler.append(Rektangel(lengde, bredde))

for rektangel in rektangler:
    print(rektangel.areal())

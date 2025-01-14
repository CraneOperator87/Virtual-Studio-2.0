Vaermelding = {
    "by": "Nesbru",
    "dato": "06/10/2023",
    "nedbor": "0",
    "gjvindstyrk": "3",
    "makstemp": "15",
    "mintemp": "10"
}

print("Dagens værmelding!\n")
print(f"Dagnes dato :{Vaermelding['dato']}")
print(f"Ved å se på byen {Vaermelding['by']}")
print(f"Ser vi at maksimal temperattur er på {Vaermelding['makstemp']} grader, og minste temperatur på {Vaermelding['mintemp']} grader!")
print(f"Det er ikke mye vindstyrke i dag, vindstyrken er på {Vaermelding['gjvindstyrk']} meter per sekund")
print(f"Og det ser til å ikke være så mye nedbør, rundt {Vaermelding['nedbor']} mm")
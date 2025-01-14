import random

magisk_tall = random.randint(1,100)
forsok = 0

try:
    while True:
        gjett = int(input("Gjett hva det magiske tallet er! (1 - 100): "))
        
        if gjett == magisk_tall:
            print(f"Gratullerer! Du fant ut at det var tallet {magisk_tall}, med {forsok} forsøk!")
            break
        elif gjett < magisk_tall:
            print(f"Ikke helt, det magiske tallet er større!")
        elif gjett > magisk_tall:
            print(f"Ikke helt, det magiske tallet er mindre!")
            
        forsok += 1

except ValueError:
    print(f"Din data er ugydildig, prøv på nytt.")
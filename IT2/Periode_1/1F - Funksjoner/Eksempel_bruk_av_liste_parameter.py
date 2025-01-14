tall1 = [9,8,7,6,5,4]
tall2 = [6,5,4,3,2,1]
tall3 = [1,2,3,4,5,6]

def endretall(liste):
    liste[0] = "test"
    print(liste)

print(tall1)
endretall(tall3)
print(tall2)

print("Hei", end= " ")
print("på deg!")
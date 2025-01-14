import numpy as np  

vektor1 = np.array([5,6])
vektor2 = np.array([-4,3])

vektortvers = np.array([3,-4])

x = np.dot(vektor1, vektor2)

print(f"Skalarproduktet av vektorene er {x}")

if x == 0:
    print("Vektorene er ortogonale, trekanten er rettvinklet!")
elif x > 0:
    print("Vektorene er ikke ortogonale, trekanten er spiss!")
else:
    print("Vektorene er ikke ortogonale, trekanten er stump!")

T = 0.5 * np.abs(vektor1 * vektortvers)
print(f"Arealet av trekanten er {T}")
hypotenus = np.sqrt(vektor1[0]**2 + vektor1[1]**2) + np.sqrt(vektor2[0]**2 + vektor2[1]**2)

omkrets = np.sqrt(vektor1[0]**2 + vektor1[1]**2) + np.sqrt(vektor2[0]**2 + vektor2[1]**2) + hypotenus
print(f"Omkretsen av trekanten er {omkrets}")







# R1 Vår 2022 Eksamen
import numpy as np


a_input = int(input("Skriv inn x kordinat (a) : ")) # x
b_input = int(input("Skriv inn y kordinat (b) : ")) # y
A = (a_input, b_input)
print(A)

c_input = int(input("Skriv inn x kordinat (c) : ")) # x
d_input = int(input("Skriv inn y kordinat (d) : ")) # y
B = (c_input, d_input)
print(B)

e_input = int(input("Skriv inn x kordinat (e) : ")) # x
f_input = int(input("Skriv inn y kordinat (f) : ")) # y
C = (e_input, f_input)
print(C)


AB =  np.array([c_input - a_input , d_input - b_input])
BC =  np.array([e_input - c_input , f_input - d_input])

print(f"Vektor AB : {AB}")
print(f"Vektor BC : {BC}")

skalarprodukt = AB[0] * BC[0] + AB[1] * BC[1]
print(f"Skalarproduktet av vektorene AB og BC = {skalarprodukt}")
if skalarprodukt == 0:
    print(f"Vektorene er ortogonale, punktene danner en rettvinklet trekant!")
else:
    print(f"Vektorene er ikke ortogonale, punktene danner ikke en rettvinklet trekant!")
    
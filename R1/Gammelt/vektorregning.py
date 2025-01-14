import numpy as np  

# Vektor AB
AB = np.array([4, 3]) # Våres vektorer

# Vektor CD
CD = np.array([8, 4]) 

# Oppgave 1
def vektor(A,B):
    return (B[0] - A[0], B[1] - A[1])

# Oppgave 1.1
def posisjonvektor(A,B):
    # X2 - X1, Y2 - Y1
    return (B[0] - A[0], B[1] - A[1]) 

def lengde_vektor(v):
    # sqrt(x^2, y^2)
    return np.sqrt(v[0]**2 + v[1]**2)

# Oppgave 1.3
def vektor_3_ganger(A,B):
    # 3 * OA og 3 * OB = 3 * (OA + OB)
    return (3 * posisjonvektor(A,B))

# Oppgave 1.4
def vektor_motsatt_5_ganger(A,B):
    # -5 * OA og -5 * OB = -5 * (OA + OB)
    return (-5 * posisjonvektor(A,B))

# Oppgave 1.5
def vektor_mostatt_en_halv(A,B):
    return (-0.5 * posisjonvektor(A,B))

# Oppgave 1.6
def vektor_25_prosent(A,B):
    return(1.25 * posisjonvektor(A,B))


# Oppgave 2
def sirkel_radius(P, S, r):
    # (x - x1)^2 + (y - y1)^2 = r^2
    # P = (x, y) og S = (x1, y1), P er et punkt, og S er sentrum av sirkelen
    if (P[0] - S[0])**2 + (P[1] - S[1])**2 == r**2:
        return True
    elif (S[0] - P[0])**2 + (S[1] - P[1])**2 > r**2:
        return ("Punktet ligger utenfor sirkelen")
    else:
        return ("Punktet ligger innenfor sirkelen")
    
# Oppgave 3
def ortogonalvinkel(A,B):
    if A[0] * B[0] + A[1] * B[1] == 0:
        return "Vinkelen er rettvinklet, vektorene er ortogonale"
    elif A[0] * B[0] + A[1] * B[1] > 0:
        return "Vinkelen er spiss, vektorene er ikke ortogonale"
    else:
        return "Vinkelen er stump, vektorene er ikke ortogonale"
    
# Oppgave 4
def rettlinjet(A,B,C):
    AB = vektor(A,B)
    BC = vektor(B,C)
    if AB[0] * BC[1] - AB[1] * BC[0] == 0:
        return "Linjene er parallelle"
    else:
        return "Linjene er ikke parallelle"


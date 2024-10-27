def f(x): return 2 * x + 1 # funksjonen f(x) = 2x + 1

def arealsum(n):
    areal = 0
    delta_x = (5 - 0) / n # Bredde til hver rektangel : Delta X = (b - a) / n

    for i in range(n):
        hoyde = f (i * delta_x) # Høyde til rektangel i
        areal = areal + hoyde * delta_x 
    return areal

print(f"n = 5: {arealsum(5)}")
print(f"n = 10: {arealsum(10)}")
print(f"n = 100: {arealsum(100)}")

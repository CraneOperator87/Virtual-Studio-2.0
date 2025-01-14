def f(x):
    return x**3 - 5*x**2 + 2

def d(x):
    return 3*x**2 - 10*x

x = 1 #Startverdi

while abs(f(x)) > 0.0000001:
    x = x - f(x)/d(x)
    
print("Løsningen er x=", round(x,5))
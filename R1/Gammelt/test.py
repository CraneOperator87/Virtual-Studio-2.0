def f(x):
    return 2*x**2 - 9*x - 2

def df(x,h):
    return (f(x+h) - f(x))/ (h)

h = 0.00001
a = 0.0

while df(a,h) < 0:
    a = a + h

print("bunnpunkt er x = ", (a, f(a)))
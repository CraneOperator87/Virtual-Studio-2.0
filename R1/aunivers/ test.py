def f(x):
    return x / (1+x**2)

h = 0.0001
x = 0

while (f(x+h) - f(x))/h > 0:
    x = x + 0.01

print("x = ", x)



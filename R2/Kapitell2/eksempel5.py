
a = -2
b = 2
n = 10

def f(x):
    return (4 - x**2)**(1/2)

summen = 0
delta_x = (b-a)/n 

for i in range(1, n+1):
    summen = summen + f(a + i * delta_x) * delta_x

print(round(summen, 1))
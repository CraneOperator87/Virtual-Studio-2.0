a = 0
b = 1
n = 10

def f(x):
    return (1 + x**2)**(1/2)

summen = 0
delta_x = (b-a)/n 

for i in range(n):
    summen = summen + f(a + i * delta_x) * delta_x

print(round(summen, 3))


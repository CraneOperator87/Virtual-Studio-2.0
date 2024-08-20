a = 1
b = 1
n = 50

print(a)
print(b)

for i in range(n):
    c = a + b
    print(c)
    print(c/b)
    a = b
    b = c
    


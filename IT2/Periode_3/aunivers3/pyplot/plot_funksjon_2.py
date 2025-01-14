import matplotlib.pyplot as plt

def f(x):
  return x**2

xverdier = [xverdi for xverdi in range(10)]
yverdier = [f(xverdi) for xverdi in xverdier]

plt.plot(xverdier, yverdier)
plt.show()
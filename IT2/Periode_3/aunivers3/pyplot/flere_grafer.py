import matplotlib.pyplot as plt  
import numpy as np 

xverdier = np.linspace(-3, 3, 50)

# Graf 1
yverdier = 0.5 * xverdier ** 2
plt.subplot(2, 1, 1)
plt.grid()
plt.plot(xverdier, yverdier)

# Graf 2
yverdier = 2 * xverdier ** 3
plt.subplot(2,1,2)
plt.grid()
plt.plot(xverdier,yverdier)

plt.show()
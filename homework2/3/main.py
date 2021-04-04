import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 50)

y = (x ** 3) - (x ** 2)


print(x)
print(y)
plt.plot(x, y , 'ro-')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-8,8)
plt.grid(True)
plt.show()



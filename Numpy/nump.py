import numpy as np
import math as ma
import matplotlib.pyplot as plt
plt.style.use("seaborn")

a = np.linspace(1,2*ma.pi, 100)
e = np.linspace(0,1, 100)
print(a)
# b = np.sin(a)
# c = np.cos(a)
# d = np.tan(a)

# d = ma.log(i for i in a)
# print(d)
d = [ma.log(i) for i in a]
exp = [ma.exp(i) for i in a]

# plt.plot(a,b)
# plt.plot(a,c)
# plt.plot(a,d)
plt.plot(a,exp)
# plt.plot(a,c)

plt.show()

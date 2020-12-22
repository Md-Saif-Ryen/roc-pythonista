import matplotlib.pyplot as plt

plt.style.use("seaborn-dark")

x = [1,5,2,6,8,3,0,5,8,9,3,7,9,4,2]
y = [4,7,8,3,9,4,7,9,7,3,1,4,7,9,3]
color = [2,5,7,8,5,5,8,7,1,3,6,7,9,2,3]
sizes = [212,311,563,122,274,163,478,309,123,531,264,196,275,163,276]
plt.scatter(x,y,s=sizes,c=color,cmap="Blues")
cbar = plt.colorbar()
cbar.set_label("Satisfaction")
plt.savefig("My Awesome scatters.png")
plt.show()
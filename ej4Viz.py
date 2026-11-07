import matplotlib.pyplot as plt

ventas=[1500,1800,2020,2080,2500,2000,1900,2300,3220,3500,3455,4500]

plt.hist(ventas,bins=5,color="orange")

plt.savefig("hist.png")

plt.show()
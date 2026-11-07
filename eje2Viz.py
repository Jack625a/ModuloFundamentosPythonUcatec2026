import matplotlib.pyplot as plt

meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto"]
ventas=[1500,1800,2020,2080,2500,2000,1900,2300]

plt.bar(meses,ventas,color="red")
plt.title("Ventas Mensuales")
plt.xlabel("Meses")
plt.ylabel("Ventas")

plt.show()
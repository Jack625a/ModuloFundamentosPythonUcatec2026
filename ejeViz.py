import matplotlib.pyplot as plt

meses=["Enero","Febrero","Marzo","Abril","Mayo"]
ventas=[1500,1800,2020,2080,2500]

plt.plot(meses,
         ventas,
         color="green",
         #linestyle=""
         marker="o",
         linewidth=3
         
         )
plt.title("VENTAS MENSUALES")
plt.xlabel("Meses")
plt.ylabel("Cantida de Ventas")

#Cuadricula
plt.grid(True)

plt.show()
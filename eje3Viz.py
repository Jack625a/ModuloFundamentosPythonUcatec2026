import matplotlib.pyplot as plt

meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
ventas=[1500,1800,2020,2080,2500,2000,1900,2300,3220,3500,3455,4500]

plt.pie(
    ventas,
    labels=meses,
    autopct="%1.1f%%"
)
plt.title("VENTAS")

plt.show()

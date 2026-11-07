import pandas as pd
import matplotlib.pyplot as plt

datos={
    "Producto":["Laptop","Celular","Televisor"],
    "Precio":[2900,1800,3500],
    "Cantidad":[2,10,15]
}

data=pd.DataFrame(datos)

print(data)

ventas=data.groupby("Producto")["Cantidad"].sum()

#Graficar (Barras)
ventas.plot(kind="bar")
#Titulo
plt.title("Total de ventas por producto")
#Eje x - texto
plt.xlabel("Producto")
#Eje y - texto
plt.ylabel("Cantidad Vendida")

#Mostrar la grafica
plt.show()
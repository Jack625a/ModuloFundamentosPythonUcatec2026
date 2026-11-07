import matplotlib.pyplot as plt

meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
ventas=[1500,1800,2020,2080,2500,2000,1900,2300,3220,3500,3455,4500]
gastos=[200,800,300,350,550,180,850,350,368,400,800,456]
productos=["Producto1","Producto2","Producto3","Producto4","Producto5"]
cantidad=[20,15,80,50,25]

#Creacion de varias graficas en uno subplot
figura,ax=plt.subplots(2,2,figsize=(12,8))

#Grafica 1
ax[0,0].plot(meses,ventas)
ax[0,0].set_title("Ventas")
#Grafico 2

ax[0,1].bar(meses,gastos)
ax[0,1].set_title("Gastos")

ax[1,0].pie(cantidad,labels=productos, autopct="%1.1f%%")
ax[1,0].set_title("Productos")

ax[1,1].scatter(meses,ventas)
ax[1,1].set_title("Ventas mensuales")

plt.tight_layout()

plt.show()
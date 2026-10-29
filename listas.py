#Conjunto de datos ordenados o desordenados que mutables
colores=["Rojo","Amarillo","Azul","Verde"]
print(colores)

#Acceder a elementos especificos
print(colores[0])
print(colores[1])
print(colores[2])
#Para mostrar el primer elemento de una lista[0]
#Para mostrar el ultimo elemento de una lista[-1]
print(colores[-1])

#Agregado de datos a una lista
#1. Agregar al final de la lista (append())
colores.append("Cafe")
print(colores)
#2. Agregar un dato en una posicion especifica (insert())
colores.insert(1,"Blanco")
print(colores)
#3. Agregar varios elementos (extend())
colores.extend(["Negro","Violeta","Anaranjado"])
print(colores)

#Modificar datos
colores[2]="Dorado"
print(colores)

#Eliminacion de datos
#Eliminacion de un valor especifico (remove())
colores.remove("Azul")
print(colores)
#Eliminacion de un dato por su posicion (pop())
colores.pop()
colores.pop(0)
print(colores)



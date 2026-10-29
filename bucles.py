#Bucles iterativos for
#for iteraciones in range(inicio,final,incremento):
for numero in range(1,100,1):
    print(numero)

#Mostrar los numeros pares hasta el 100
for pares in range(1,100,2):
    print(pares)

#RECORRIDO EN UNA LISTA
estudiantes=["Kevin","Ana","Juan","Jose","Maria"]
for estudiante in estudiantes:
    print("Estudiante: ",estudiante)

notas=[85,25,45,85,96,12,25,45,66]
suma=0
for nota in notas:
    suma=suma+nota

promedio=suma/len(notas)
print("Promedio: ",promedio)

#Controlar los bucles o romper el bucle (break)
for numero in range(1,100):
    if numero==85:
        break
    print(numero)

#Saltar una iteracion (continue)
for n in range(1,11):
    if n==8:
        continue
    print(n)


#Bucles anidados
#for iteracion in range(i,f,in):
    #for iteracion in range(i,f,in):

for fila in range(1,8):
    for columna in range(1,8):
        print(columna,end=" ")
    print()






#Bucles Condicionados while
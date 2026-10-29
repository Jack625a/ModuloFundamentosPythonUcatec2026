a=15
b=20
if a>b:
    print("El mayor es: ",a)
else:
    print("El mayor es", b)

#Varias condiciones para evaluacion (elif)
#Obtener 3 notas del estudiantes y determinar el promedio
#informando la nota y el estado de su calificacion
# mayor a 90 Excelente
#mayor o igual a 75 Bueno
#mayor o igual a 51 Regular
#menor a 51 Reprobado
n1=int(input("Ingrese la nota: "))
n2=int(input("Ingrese la nota: "))
n3=int(input("Ingrese la nota: "))
promedio=(n1+n2+n3)/3
if promedio>=90:
    print(f"Estado Aprobado - Nota: {promedio} Excelente")
elif promedio>=75:
    print(f"Estado Aprobado - Nota {promedio} Bueno")
elif promedio>=51:
    print(f"Estado Aprobado - Nota {promedio} Regular")
else:
    print(f"Estado Reprobado - Nota {promedio}")


#Condicionales - Operadores Logicos (y-and, o-or, no-not)

edad=int(input("Ingrese su edad: "))
ingreso=True

if edad>=18 and ingreso:
    print("Puede acceder")
else:
    print("No puede ingresar")
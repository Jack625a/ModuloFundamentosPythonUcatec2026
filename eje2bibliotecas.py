#DATAFRAME
import pandas as pd
datos={
    "codEstudiante":[111,222,333,444],
    "nombre":["Kevin","Juan","Jose","Ana"],
    "edad":[30,25,26,20],
    "nota":[85,75,55,90]
}

dataFrame=pd.DataFrame(datos)
print(dataFrame[["edad","nombre"]])

#Para acceder a filas .iloc
print(dataFrame.iloc[2])

#Para acceder a etiquetas .loc
print(dataFrame.loc[0])

nuevosDatos={
    "codEstudiante":555,
    "nombre":"Carlos",
    "edad":21,
    "nota":85
}
dataFrame.loc[len(dataFrame)]=nuevosDatos

print(dataFrame)

#Mostrar la desviacion estandar
print(dataFrame["nota"].std())
#Media
print(dataFrame["nota"].median())

#Nuevos datos en posiciones especificas
#dataFrame.loc[0]=[666,"Maria",20,75]
#print(dataFrame)

#Nuevos datos en una columna especifica .set_index("columna")
#dataframe=dataFrame.set_index("codEstudiante")
print(dataFrame)

#dataFrame=dataFrame.set_index("codEstudiante")
#dataFrame.loc[0]=[745,"Jesus",26,95]

nuevo=pd.DataFrame({
    "codEstudiante":[745],
    "nombre":["Jesus"],
    "edad":[26],
    "nota":[95]
})

#INSERTAR EN LA POSICION 1
dataFrame=pd.concat([
    dataFrame.iloc[:3],
    nuevo,
    dataFrame.iloc[3:]
], 
    ignore_index=True
)

print(dataFrame)

#INSERTAR EN LA POSICION 1
dataFrame=pd.concat([
    nuevo,
    dataFrame
], 
    ignore_index=True
)

print(dataFrame)


#Dimension de los dataframe .shape()
print(dataFrame.shape)
#Tipos de datos de un dataFrame .info
print(dataFrame.info())
#OBTENCION DE DATOS ESTADISTICOS GENERALES .describe()
print(dataFrame.describe())
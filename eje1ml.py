import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

datos={
    "horasEstudio":[2,3,4,5,6,7,8,9,10],
    "asistencia":[50,55,60,65,70,75,85,95,20],
    "aprobado":[0,0,0,0,1,1,1,1,1]
}
df=pd.DataFrame(datos)
print(df)

#Separacion de variables de entrada con la variable objetivo
x=df[["horasEstudio","asistencia"]]
y=df["aprobado"]

#division de datos para entrenamiento y datos para pruebas
xEntrenamiento,xPrueba,yEntrenamiento,yPrueba=train_test_split(
    x,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
#Creacion de un modelo de machine learning
modelo=DecisionTreeClassifier()

#entrenamiento del modelo .fit()
modelo.fit(xEntrenamiento,yEntrenamiento)

#prediccion de efectividad del modelo
predicciones=modelo.predict(xPrueba)
print(predicciones)
efeciencia=accuracy_score(yPrueba,predicciones)
print("Exactitud: ",efeciencia*100,"%")

estudiantes=[
                [1,80],
                [8,20],
                [2,40],
                [5,70],
                [8,95],
                #[10,100]
             ]
resultado=modelo.predict(estudiantes)
print("Resultado: ",resultado)
#efeciencia=accuracy_score(yPrueba,resultado)
#print("Exactitud: ",efeciencia*100,"%")
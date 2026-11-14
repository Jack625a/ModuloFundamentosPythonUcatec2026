#REGRESIONES LOGISTICAS
#CLASIFICATORIO
#REGRESIONES
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline

datos={
    "horaEstudio":[1,2,1,3,2,4,5,3,6,7,10],
    "asistencia":[30,40,35,50,45,80,85,50,90,100,20],
    "estado":[0,0,0,0,1,0,1,0,1,1,1] #0 reprobado 1 aprobado 
}
df=pd.DataFrame(datos)
print(df)

#Separacion de variables
x=df[["horaEstudio","asistencia"]] #variables de entrada
y=df["estado"] 
xEntrenamiento,xPrueba,yEntrenamiento,yPrueba=train_test_split(
    x,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

#Crear el modelo
modelo=make_pipeline(
    StandardScaler(),
    LogisticRegression()
)
modelo.fit(xEntrenamiento,yEntrenamiento)

predicciones=modelo.predict(xPrueba)
precision=accuracy_score(yPrueba,predicciones)
print("Resultados reales: ", yPrueba.values)
print("Resultados de la prediccion: ",predicciones)
print("Precision: ",precision*100,"%")

nuevoDato=pd.DataFrame({
    "horaEstudio":[7,6,2,9,11],
    "asistencia":[85,55,30,25,10]
})

resultado=modelo.predict(nuevoDato)
probabilidades=modelo.predict_proba(nuevoDato)
print("Predicciones: ",resultado)
print("Probabilidades: ",probabilidades)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score,mean_squared_error
import matplotlib.pyplot as plt

datos={
    "metros":[40,50,60,70,80,90,100],
    "antiguedad":[20,11,9,10,8,5,2],
    "cantidadHabitaciones":[1,2,2,2,3,3,4],
    "precio":[100000,125000,180000,215000,250000,280000,300000]
}

df=pd.DataFrame(datos)
print(df)
#separacion de variables
x=df[["metros","antiguedad","cantidadHabitaciones"]]
y=df["precio"]

xEntrenamiento,xPrueba,yEntrenamiento,yPrueba=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
#crear el modelo
modelo=LinearRegression()
#entrenar el modelo
modelo.fit(x,y)
#predecir 
nuevodato=pd.DataFrame({
    "metros":[85],
    "antiguedad":[25],
    "cantidadHabitaciones":[3]
})

predicciones=modelo.predict(xPrueba)
prediccion=modelo.predict(nuevodato)
print("Precio Estimado: ",prediccion)
metrica1=mean_absolute_error(yPrueba,predicciones)
metrica2=r2_score(yPrueba,predicciones)
metrica3=mean_squared_error(yPrueba,predicciones)

print("Error absoluto medio= ",metrica1)
print("Coeficiente de variabilidad= ",metrica2)
print("Error cuadratico medio= ",metrica3)

plt.scatter(x["metros"],y,label="Datos reales")
plt.plot(
    x["metros"],
    modelo.predict(x),
    color="red",
    label="Prediccion del modelo"
)
plt.legend()

plt.show()
import keras
import numpy as np

#paso 1. datos de entrada
x=np.array([
    [1],[2],[3],[4],[5],[6],[7],[8]
])
y=np.array([
    [0],[0],[0],[0],[1],[1],[1],[1]
]) #0 reprobado 1 aprobado

#paso 2. crear la red neuronal
modelo=keras.Sequential([
    #definir los datos de entrada
    keras.Input(shape=(1,)),
    #definir la cantidad de neuronas
    keras.layers.Dense(8,activation="relu"),
    #crear la capa saliente (neurona de salida)
    keras.layers.Dense(1,activation="sigmoid")
])

#paso 3. Compilar el modelo
modelo.compile(
   optimizer="adam",
   loss="binary_crossentropy",
   metrics=["accuracy"]
)
#Paso 4. entrenar modelo
modelo.fit(
    x,
    y,
    epochs=1000,
)
ejemploPrueba=np.array([[6]])
resultado=modelo.predict(ejemploPrueba)
print(resultado)
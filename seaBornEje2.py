import seaborn as se
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#datos={
 #   "Programacion":[90,85,75,92,90],
  #  "Calculo":[95,100,75,60,85],
   # "Estadistica":[85,75,70,90,80]
#}

#df=pd.DataFrame(datos)
notas=pd.DataFrame(
    np.random.randint(35,101,(10,5)),
    columns=[
        "Programacion",
        "Base de Datos",
        "Calculo",
        "Estadistica",
        "Redes"
    ],
    index=[f"Estudiante {i}" for i in range(1,11)]
)

print(notas)

se.heatmap(
    notas,
    annot=True
)

plt.show()
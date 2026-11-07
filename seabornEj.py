#Desempeño de estudinates
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as se

datos={
    "Estudiante":["Kevin","Juan","Ana","Sofia","Jose","Maria","Luis"],
    "Nota":[85,60,95,75,80,90,80]
}

df=pd.DataFrame(datos)
print(df)
se.histplot(
    data=df,
    x="Nota"
)

plt.title("Distribucion de notas")
plt.xlabel("Notas")
plt.ylabel("Estudiantes")

plt.show()
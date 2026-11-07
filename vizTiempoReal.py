import matplotlib.pyplot as plt
import matplotlib.animation as an
import random
from collections import deque

datosX=deque(maxlen=100)
datosY=deque(maxlen=100)

contador=0

fig,ax=plt.subplots()

ax.set_title("Monitor de datos en tiempo real")
ax.set_xlim(0,100)
ax.set_ylim(0,99)
ax.grid(True)
linea, =ax.plot([],[], marker="o", color="red",label="Datos")

ax.legend()

def actualizacionDatos(frame):
    global contador
    nuevoDatos=random.randint(0,100)

    datosX.append(contador)
    datosY.append(nuevoDatos)

    contador=contador+1

    linea.set_data(
        range(len(datosY)),datosY
    )

    return (linea,)

animacion=an.FuncAnimation(
    fig,
    actualizacionDatos,
    interval=1000,
    blit=False,
    cache_frame_data=False
)

plt.tight_layout()
plt.show()
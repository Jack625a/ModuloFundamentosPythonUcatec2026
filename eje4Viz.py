import matplotlib.pyplot as plt

meses=[1,2,3,4,5,6,7,8,9,10,11,12]
ventas2026=[1800,2020,2080,2200,2400,2800,2900,2300,3220,3600,3555,3500]
ventas2025=[1500,1800,2020,2080,2500,4000,1900,2300,3220,3500,3455,4500]

plt.plot(meses,ventas2025, label="2025", color="red")
plt.plot(meses,ventas2026, label="2026", color="blue")

plt.title("Comparacion de Ventas")
plt.xlabel("Meses")
plt.ylabel("Ventas")
plt.grid(True)
plt.legend()

plt.show()
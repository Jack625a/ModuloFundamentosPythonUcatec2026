import seaborn as se
import matplotlib.pyplot as plt

datos=se.load_dataset("planets")

se.pairplot(
    datos,
    hue="method"
)
plt.show()
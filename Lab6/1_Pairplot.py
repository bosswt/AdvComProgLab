import pandas as pd
import seaborn as sbs
import matplotlib.pyplot as plt

df = pd.read_csv("Iris.csv")
sbs.pairplot(
    df,
    hue="Species",
    vars=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"],
)
plt.show()

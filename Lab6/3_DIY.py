import pandas as pd
import seaborn as sbs
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")
sbs.barplot(data=df, x="Pclass", y="Survived", estimator=sum)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")
pd.pivot_table(df, index="Survived", columns="Sex", aggfunc="count")["Name"].reindex(
    ["male", "female"], axis=1
).plot(kind="bar")
plt.show()

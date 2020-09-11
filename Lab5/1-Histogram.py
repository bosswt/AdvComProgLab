import pandas as pd
import matplotlib.pyplot as plt

dataframes = pd.read_csv("score.csv", header=None)
dataframes.columns = ["ID", "Q1", "Q2", "Q3", "Q4", "Q5"]
dataframes["sum"] = dataframes.iloc[:, 1:].sum(axis=1)
dataframes["sum"].hist(bins=12)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pm25.csv")
df.columns = ["dt", "pm"]
filtered_df = df[df.pm != "-"]
filtered_df.dt = pd.to_datetime(filtered_df.dt)
filtered_df.pm = pd.to_numeric(filtered_df.pm)
filtered_df["dow"] = filtered_df.dt.dt.dayofweek
x = filtered_df.groupby("dow").mean().plot(kind="bar", color="green")
plt.xlabel("Day of week")
# Monday=0,Sunday=6
plt.show()

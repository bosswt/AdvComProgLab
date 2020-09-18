import pandas as pd
import seaborn as sbs
import matplotlib.pyplot as plt


def get_color(value):
    if value >= 50:
        color = "red"
    elif value >= 37:
        color = "yellow"
    else:
        color = "green"
    return color


df = pd.read_csv("pm25.csv")
df.columns = ["date", "pm"]
df = df[df["pm"] != "-"]
df["date"] = pd.to_datetime(df["date"])
df["pm"] = pd.to_numeric(df["pm"])
df["hr"] = df["date"].dt.hour
hr_mean = df.groupby("hr").mean()
hr_colors = [get_color(float(hr)) for hr in hr_mean["pm"]]
sbs.barplot(data=df, x="hr", y="pm", palette=hr_colors)
plt.show()

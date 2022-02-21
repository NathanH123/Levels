import pandas as pd
import csv
import plotly.graph_objects as pgo

df = pd.read_csv("pixel.csv")
print(df.groupby("level")["attempt"].mean())
figure = pgo.Figure(pgo.Bar(
    x = df.groupby("level")["attempt"].mean(),
    y = ["level1", "level2", "level3", "level4"],
    orientation = "h"
))
figure.show()
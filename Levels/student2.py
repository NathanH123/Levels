import pandas as pd
import csv
import plotly.graph_objects as pgo

df = pd.read_csv("pixel.csv")
studentdf = df.loc[df["student_id"] == "TRL_xsl"]
print(studentdf.groupby("level")["attempt"].mean())
figure = pgo.Figure(pgo.Bar(
    x = studentdf.groupby("level")["attempt"].mean(),
    y = ["level1", "level2", "level3", "level4"],
    orientation ="h"
))
figure.show()
import pandas as pd
import statistics 

df=pd.read_csv("data.csv")
data=df["Weight(Pounds)"].tolist()
m=statistics.median(data)
print(m)
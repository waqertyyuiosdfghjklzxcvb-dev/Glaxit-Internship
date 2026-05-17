import pandas as pd

call = pd.read_csv("task_scrap.csv")
print(call["Stock"].isnull().sum())
print(call.info())
print(call.head(10))
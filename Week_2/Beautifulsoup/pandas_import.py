import pandas as pd

call = pd.read_csv('scrap_data.csv', encoding='latin-1')

print(call.head(10))
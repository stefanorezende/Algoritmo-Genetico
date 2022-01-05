import numpy as np
import pandas as pd

df = pd.read_csv("Geracao.csv")

for i in df.index:
    arr= np.array(df.iloc[i,1:13])

print(arr)
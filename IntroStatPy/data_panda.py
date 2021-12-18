import numpy as np 
import pandas as pd 

t = np.arange(0, 10, 0.1)
x = np.sin(t)
y = np.cos(t)

df = pd.DataFrame({'Time': t, 'x': x, 'y':y})
data = df[['Time', 'y']]
print(data.head())
print(data.tail())

print(data[4:10])
print(df.iloc[4:10, [0, 2]])
print(data.values)
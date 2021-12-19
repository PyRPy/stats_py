# test file input
import numpy as np
import pandas as pd
data = np.loadtxt('data.txt', delimiter=',')
print(data)
print(type(data))

# use pandas
df = pd.read_csv('data.txt', header=None)
print(df.head())

# with headers
df2 = pd.read_csv('data2.txt', delimiter=',')
print(df2)

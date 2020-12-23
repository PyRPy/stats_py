# MANOVA test in statsmodel

import pandas as pd
from statsmodels.multivariate.manova import MANOVA
# data for t test
url = 'https://vincentarelbundock.github.io/Rdatasets/csv/datasets/iris.csv'
df = pd.read_csv(url, index_col=0)
df.columns = df.columns.str.replace(".", "_")
print(df.head())

# run the manova model
maov = MANOVA.from_formula('Sepal_Length + Sepal_Width + \
                            Petal_Length + Petal_Width  ~ Species', data=df)

# print out the results
print() # print a blank line
print(maov.mv_test())

# source
# https://www.marsja.se/python-manova-made-easy-using-statsmodels/

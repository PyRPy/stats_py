import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

import sklearn
from sklearn.linear_model import Perceptron

# load data
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['label'] = iris.target

df.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'label']
print(df.info)
# plot data
# plt.scatter(df[:50]['sepal length'], df[:50]['sepal width'], label = '0')
# plt.scatter(df[50:100]['sepal length'], df[50:100]['sepal width'], label = '1')
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.legend()
# plt.show()

# prepare data
data = np.array(df.iloc[:100, [0, 1, -1]])
X, y = data[:, :-1], data[:, -1]
y = np.array([1 if i == 1 else -1 for i in y])

# classifer from sklearn
clf = Perceptron(fit_intercept=True, max_iter=1000, shuffle=True)
clf.fit(X, y)
print('training result')
print(clf.score(X, y))

# test data set
test = np.array(df.iloc[101:, [0, 1, -1]])
X_test, y_test = test[:, :-1], test[:, -1]
y_test = np.array([1 if i == 1 else -1 for i in y_test])
print('test result')
print(clf.score(X_test, y_test))

# reference
# https://github.com/fengdu78/lihang-code/blob/master/%E7%AC%AC02%E7%AB%A0%20%E6%84%9F%E7%9F%A5%E6%9C%BA/2.Perceptron.ipynb
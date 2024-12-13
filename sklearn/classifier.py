## example in scikit learn

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import (ensemble, model_selection, preprocessing, tree)
from sklearn.metrics import (auc, confusion_matrix, roc_auc_score, roc_curve,
                             accuracy_score, classification_report
                             )
from sklearn.model_selection import (train_test_split, StratifiedKFold)
from sklearn.linear_model import LogisticRegression

## load breast cancer dataset
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y = True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
## print(X_train[0:5])
## check the data type
print("type of X_train: ", type(X_train))
print("type of y_train: ", type(y_train))

## linear classifier
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred[:10])

## evaluation
print("Accuracy: ", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("confusion matrix: \n", confusion_matrix(y_test, y_pred))

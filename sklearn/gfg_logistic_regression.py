# gfg_logistic_regression.py

from sklearn import datasets, linear_model, metrics 
from sklearn.model_selection import train_test_split 

digits = datasets.load_digits() 

X = digits.data   
y = digits.target 

X_train, X_test, y_train, y_test = train_test_split(X, y, \
                                    test_size = 0.4, random_state=1)

reg = linear_model.LogisticRegression() 
reg.fit(X_train, y_train) 

y_pred = reg.predict(X_test) 

print('logistic regression model accuracy: ', metrics.accuracy_score(y_test, y_pred))

# https://www.geeksforgeeks.org/understanding-logistic-regression/

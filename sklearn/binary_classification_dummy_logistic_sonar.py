# load the library
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.dummy import DummyClassifier

# read data
dat = pd.read_csv("Sonar.csv")

# dat.head()
print(dat.shape)

# convert 'Class' column to 'category' data type
X = dat.drop('Class', 1)
dat['Class'] = dat['Class'].astype('category')
y = dat['Class']

# split data into train / test data sets
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)

# fit the dummy model
dummyMod = DummyClassifier()
dummyMod.fit(X_train, y_train)
print("dummy baseline accuracy: {0:0.3}".format(dummyMod.score(X_test, y_test)))

# fit the logistic regression model
logReg = LogisticRegression(C=0.01, solver='liblinear').fit(X_train,y_train)

# evaluate the model on test data set
y_pred = logReg.predict(X_test)
print("Accuracy: {0:0.3}".format(metrics.accuracy_score(y_test, y_pred)))
print(confusion_matrix(y_test, y_pred))

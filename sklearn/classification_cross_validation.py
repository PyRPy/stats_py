# https://github.com/mattharrison/ml_pocket_reference
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

import warnings
warnings.filterwarnings("ignore")

### --- load data --- ###
df = pd.read_excel("Data/titanic3.xlsx")
orig_df = df

name = df.name
df = df.drop(
    columns=[
        "name",
        "ticket",
        "home.dest",
        "boat",
        "body",
        "cabin",
    ]
)

df = pd.get_dummies(df)
df = df.drop(columns="sex_male")
df = pd.get_dummies(df, drop_first=True)

# get the input data and label
y = df.survived
X = df.drop(columns = "survived")

# sample data
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size = 0.3, 
                                                    random_state = 42)

# impute data
from sklearn.experimental import enable_iterative_imputer
from sklearn import impute

num_cols = ["pclass", "age", "sibsp", "parch", "fare", "sex_female"]
imputer = impute.IterativeImputer()
imputed = imputer.fit_transform(X_train[num_cols])

X_train.loc[:, num_cols] = imputed
imputed = imputer.transform(X_test[num_cols])
X_test.loc[:, num_cols] = imputed

meds = X_train.median()
X_train = X_train.fillna(meds)
X_test = X_test.fillna(meds)

# Normalize data
cols = ['pclass', 'age', 'sibsp', 'parch', 'fare', 'sex_female', 'embarked_C',
       'embarked_Q', 'embarked_S']

sca = preprocessing.StandardScaler()
X_train = sca.fit_transform(X_train)
X_train = pd.DataFrame(X_train, columns=cols)
X_test = sca.transform(X_test)
X_test = pd.DataFrame(X_test, columns=cols)

# Baseline model
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
bm = DummyClassifier()
bm.fit(X_train, y_train)
bm.score(X_test, y_test)  # accuracy
print("baselne model: ", bm.score(X_test, y_test))

lr = LogisticRegression()
lr.fit(X_train, y_train)
lr.score(X_test, y_test)
print("logistic regression: ", lr.score(X_test, y_test))

# Confusion matrix
from sklearn.metrics import confusion_matrix
y_pred = lr.predict(X_test)
print("confusion matrix: ")
print(confusion_matrix(y_test, y_pred))

# Various model using cross-validation
X = pd.concat([X_train, X_test])
y = pd.concat([y_train, y_test])

from sklearn import model_selection
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

# loop over a list of models
model_list = [DummyClassifier, LogisticRegression, DecisionTreeClassifier,
                KNeighborsClassifier, GaussianNB, SVC, RandomForestClassifier]
print("Classifiers in sklearn based models: ")
for model in model_list:
    cls = model() 
    kfold = model_selection.KFold(n_splits=5, random_state=42)
    s = model_selection.cross_val_score(cls, X, y, scoring="roc_auc", cv = kfold)
    print(f"{model.__name__:22} AUC: " 
          f"{s.mean():.3f} STD: {s.std():.2f}")

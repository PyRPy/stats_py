# https://github.com/mattharrison/ml_pocket_reference
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

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
bm = DummyClassifier()
bm.fit(X_train, y_train)
bm.score(X_test, y_test)  # accuracy
print("baselne model: ", bm.score(X_test, y_test))

# Various model families
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr.score(X_test, y_test)
print("logistic regression: ", lr.score(X_test, y_test))

# Confusion matrix
from sklearn.metrics import confusion_matrix
y_pred = lr.predict(X_test)
print("confusion matrix: ")
print(confusion_matrix(y_test, y_pred))

# Deploy model
import pickle
pic = pickle.dumps(lr)
lr2 = pickle.loads(pic)
y_pred2 = lr2.predict(X_test)
print(confusion_matrix(y_test, y_pred2))
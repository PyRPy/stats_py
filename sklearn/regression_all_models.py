# https://github.com/mattharrison/ml_pocket_reference
# https://scikit-learn.org/stable/modules/cross_validation.html
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

# remove warnings
import warnings
warnings.filterwarnings("ignore")

### --- load data --- ###
from sklearn.datasets import load_boston
b = load_boston()
bos_X = pd.DataFrame(b.data, columns=b.feature_names)
bos_y = b.target
bos_X_train, bos_X_test, bos_y_train, bos_y_test = train_test_split(
    bos_X,
    bos_y,
    test_size=0.3,
    random_state=42,
)
bos_sX = preprocessing.StandardScaler().fit_transform(
    bos_X
)
bos_sX_train, bos_sX_test, bos_sy_train, bos_sy_test = train_test_split(
    bos_sX,
    bos_y,
    test_size=0.3,
    random_state=42,
)

# Baseline model
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
br = DummyRegressor()
br.fit(bos_X_train, bos_y_train)
br.score(bos_X_test, bos_y_test)  # accuracy
print("baselne model: ", br.score(bos_X_test, bos_y_test))

lr = LinearRegression()
lr.fit(bos_X_train, bos_y_train)
lr.score(bos_X_test, bos_y_test)  # accuracy
print("linear model: ", lr.score(bos_X_test, bos_y_test))


# Various model using cross-validation
from sklearn import model_selection
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor

# loop over a list of models
model_list = [DummyRegressor, LinearRegression, DecisionTreeRegressor, 
                KNeighborsRegressor, SVR, RandomForestRegressor]
print("regression in sklearn based models: ")
for model in model_list:
    regs = model() 
    res = model_selection.cross_val_score(regs, bos_X, bos_y, cv = 5)
    print(f"{model.__name__:22} score : " f"{res.mean():.3f}")

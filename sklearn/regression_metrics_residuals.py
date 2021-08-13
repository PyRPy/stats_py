# https://github.com/mattharrison/ml_pocket_reference
# https://scikit-learn.org/stable/modules/cross_validation.html
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import metrics 

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


# use random forest as a 'new' regression model
from sklearn import model_selection
from sklearn.ensemble import RandomForestRegressor

rfr = RandomForestRegressor(random_state=42, n_estimators=100)
rfr.fit(bos_X_train, bos_y_train)

bos_y_test_pred = rfr.predict(bos_X_test)

# R2
print("Random Forest for regression: ")
print("R2: ", metrics.r2_score(bos_y_test, bos_y_test_pred))

print("Mean squared error: ", metrics.mean_squared_error(bos_y_test, bos_y_test_pred))

# Residuals plot
import statsmodels.stats.api as sms 
resids = bos_y_test - rfr.predict(bos_X_test)

from scipy import stats
fig, ax = plt.subplots(figsize = (6, 4))
_ = stats.probplot(resids, plot=ax)
plt.show()

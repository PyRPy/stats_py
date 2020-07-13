# gfg_pca.py
# step 1 import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import data set
dataset = pd.read_csv('Wine.csv')
print(dataset.head())

# divide data into X and y colomns
X = dataset.iloc[:, 1:13].values
y = dataset.iloc[:, 13].values

# step 3 split data into training and testing parts
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, \
                                                    random_state = 0)

# scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

print(X_train[1:2])
print(X_test[1:2])

# step 5 apply PCA function
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)
explained_variance = pca.explained_variance_ratio_

# fit logistic regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# step 7 prediction
y_pred = classifier.predict(X_test)

# step 8 confustion matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print('confusion matrix: ')
print(cm)
print('accuracy: {: .3f}'.format(accuracy_score(y_test, y_pred)))

# step 9 predict the training data set
##from matplotlib.colors import ListedColormap
##X_set, y_set = X_train, y_train
##
##X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, 
##                     stop = X_set[:, 0].max() + 1, step = 0.01), 
##                     np.arange(start = X_set[:, 1].min() - 1, 
##                     stop = X_set[:, 1].max() + 1, step = 0.01)) 
##  
##plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), 
##             X2.ravel()]).T).reshape(X1.shape), alpha = 0.75, 
##             cmap = ListedColormap(('yellow', 'white', 'aquamarine'))) 
##  
##plt.xlim(X1.min(), X1.max()) 
##plt.ylim(X2.min(), X2.max()) 
##  
##for i, j in enumerate(np.unique(y_set)): 
##    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], 
##                c = ListedColormap(('red', 'green', 'blue'))(i), label = j) 
##  
##plt.title('Logistic Regression (Training set)') 
##plt.xlabel('PC1') # for Xlabel 
##plt.ylabel('PC2') # for Ylabel 
##plt.legend() # to show legend 
##  
### show scatter plot 
##plt.show()

# step 10 visualizing test data set
# Visualising the Test set results through scatter plot 
from matplotlib.colors import ListedColormap 

X_set, y_set = X_test, y_test 

X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, 
					stop = X_set[:, 0].max() + 1, step = 0.01), 
					np.arange(start = X_set[:, 1].min() - 1, 
					stop = X_set[:, 1].max() + 1, step = 0.01)) 

plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), 
			X2.ravel()]).T).reshape(X1.shape), alpha = 0.75, 
			cmap = ListedColormap(('yellow', 'white', 'aquamarine'))) 

plt.xlim(X1.min(), X1.max()) 
plt.ylim(X2.min(), X2.max()) 

for i, j in enumerate(np.unique(y_set)): 
	plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], 
				c = ListedColormap(('red', 'green', 'blue'))(i), label = j) 

# title for scatter plot 
plt.title('Logistic Regression (Test set)') 
plt.xlabel('PC1') # for Xlabel 
plt.ylabel('PC2') # for Ylabel 
plt.legend() 

# show scatter plot 
plt.show() 

# https://www.geeksforgeeks.org/principal-component-analysis-with-python/

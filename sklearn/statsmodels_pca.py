# pca in statsmodels
import numpy as np
from statsmodels.multivariate.pca import PCA
X = np.random.randn(100)[:, None]
X = X + np.random.randn(100, 100)
pc = PCA(X)

print(pc.factors.shape) 
pc.plot_scree(ncomp = 5).show()

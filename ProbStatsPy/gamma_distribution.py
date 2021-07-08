# gamma distribution
# reference : The statistics and calculus with python - workshop
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

samples = np.random.gamma(1, size = 1000)

x = np.linspace(samples.min(), samples.max(), 1000)
y = stats.gamma.pdf(x, 1)

plt.hist(samples, alpha = 0.2, bins = 20, density = True)
plt.plot(x, y)
plt.show()
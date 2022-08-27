import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# normal distribution
mu = 0
var = 4
sigma = np.sqrt(var)
x = np.linspace(-10, 10, 200)
y = norm.pdf(x, mu, sigma)

# plot the density curve
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y-Probability")
plt.title("normal Distribution")
plt.show()
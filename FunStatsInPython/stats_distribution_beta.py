import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt

# Beta distribution
x = np.linspace(0, 1, 100)
y = beta.pdf(x, 10, 10)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y-Probability")
plt.title("Beta Distribution")
plt.show()i
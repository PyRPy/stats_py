# https://github.com/thomas-haslwanter/statsintro_python
# code from the book above
import numpy as np
import matplotlib.pyplot as plt

t = np.r_[0:10:0.1]

freq = 0.5
x = np.sin(2*np.pi * freq * t)

plt.plot(t, x)
plt.xlabel('Time[sec]')
plt.ylabel('Values')
plt.show()

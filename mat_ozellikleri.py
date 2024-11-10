import matplotlib
import numpy as np

matplotlib.use("TkAgg")  # Backend'i TkAgg yapıyoruz

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)

#plot
x = np.array([1,8])
y = np.array([0,150])
plt.plot(x,y)
plt.show()

plt.plot(x,y,"o")
plt.show()

#marker
y = np.array([13,28,11,100])
plt.plot(y, marker = "*")
plt.show()
#seaborn
import matplotlib
import pandas as pd
matplotlib.use("TkAgg")
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("tips")
df.head()
df["sex"].value_counts()
sns.countplot(x =df["sex"],data=df)
plt.show()

#sayısal değişken görselleştirme

sns.boxplot(x = df["total_bill"])
plt.show()
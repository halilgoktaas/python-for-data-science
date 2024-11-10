import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.tail() #sondaki değerler
df.shape #boyut bilgisi
df.info #bilgiler
df.columns #değişken isimleri
df.index
df.describe().T #özet
df.isnull().values.any() #herhangi bir boş değer var mı
df.isnull().sum() #her bir değişkende kaç tane eksik değer var
df["sex"].head()
df["sex"].value_counts()
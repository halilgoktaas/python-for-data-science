import numpy as np
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()
df.index
df[0:13]
df.drop(0,axis=0).head()
delete_indexes = [1,3,5,7]
df.drop(delete_indexes,axis=0).head(10)
#inplace kalıcı olarak siler

#değişkeni indexe çevirmek

df["age"].head()
df.age.head()

df.index=df["age"]
df.drop("age",axis=1,inplace=True)

#indexi değişkene çevirmek
df["age"] = df.index
df.reset_index().head()
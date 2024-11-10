import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None)
df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"]*2
df["age3"] = df["age"] * 5

for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())



for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10


df[["age","age2","age3"]].apply(lambda x: x/10).head()
df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x-x.mean())).head()

import numpy as np
import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None)
df = sns.load_dataset("titanic")
"age" in df
df["age"].head()
df[["age","alive"]]
col_names = ["age","adult_male","alive"]
df[col_names]

df["age2"] = df["age"] ** 2
df ["age3"] = df["age"] / df["age2"]
df.drop("age3",axis=1,inplace=True)

df.loc[:, ~df.columns.str.contains("age")].head()
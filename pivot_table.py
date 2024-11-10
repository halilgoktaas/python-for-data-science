import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None)
df = sns.load_dataset("titanic")

df.pivot_table("survived","sex","embarked")
df.pivot_table("survived","sex","embarked",aggfunc="std")
df.pivot_table("survived","sex",["embarked","class"])

df["new_age"] = pd.cut(df["age"], [0,10,18,25,40,90])
df.head()
df.pivot_table("survived","sex",["new_age","class"])
pd.set_option("display.width",500)
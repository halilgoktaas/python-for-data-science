import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None)
df = sns.load_dataset("titanic")

df[df["age"]>50].head()
df[df["age"]>50]["age"].count()

df.loc[df["age"]>50,["age","class"]].head()
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age","class"]].head()
df.loc[(df["age"] > 50) & (df["sex"] == "male") & (df["embark_town"] =="Cherbourg") , ["age","class","embark_town"]].head()


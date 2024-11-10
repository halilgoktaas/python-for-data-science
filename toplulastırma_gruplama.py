#toplulaştırma ve gruplaştırma
import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None)
df = sns.load_dataset("titanic")
df["age"].mean() #yaş ortalaması

df.groupby("sex")["age"].mean() #cinsiyete göre yaş ortalaması
df.groupby("sex").agg({"age":["mean","sum"]})

df.groupby("sex").agg({"age":["mean","sum"],"survived":"mean"})

df.groupby(["sex","embark_town"]).agg({"age":["mean"], "survived": "mean"})





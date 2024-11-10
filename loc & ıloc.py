import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None)
df = sns.load_dataset("titanic")
#iloc
df.iloc[0:3]

#loc
df.loc[0:3]

df.iloc[0:3,0:3]
df.loc[0:3,"age"]
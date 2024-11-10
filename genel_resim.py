#genel resim

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")
df.head()

def check_df(dataframe,head=5):
    print("########## Shape ###########")
    print(dataframe.shape)
    print("###### Types ######")
    print(dataframe.dtypes)

check_df(df)

df = sns.load_dataset("tips")
check_df(df)
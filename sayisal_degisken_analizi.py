import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sympy import numer

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")
df.head()


df[["age","fare"]].describe().T

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]

num_but_cat =  [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int","float","bool"]]

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in["category","object"]]

cat_cols = cat_cols + num_but_cat

num_cols = [col for col in df.columns if df[col].dtypes in ["int","float"]]

num_cols = [col for col in num_cols if col not in cat_cols]


def new_summary(dataframe,numerical_tool):
    quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,0.95,0.99]
    print(dataframe[numerical_tool].describe(quantiles).T)

new_summary(df, "age")

for col in num_cols:
    new_summary(df,col)


def new_summary(dataframe,numerical_tool,plot=False):
    quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,0.95,0.99]
    print(dataframe[numerical_tool].describe(quantiles).T)

    if plot:
        dataframe[numerical_tool].hist()
        plt.xlabel(numerical_tool)
        plt.title(numerical_tool)
        plt.show(block=True)

new_summary(df, "age", plot=True)

for col in num_cols:
    new_summary(df,col,plot=True)

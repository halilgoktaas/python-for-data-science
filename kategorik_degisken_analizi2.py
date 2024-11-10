import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")
df.head()


def cat_summary(dataframe,col_name,plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")


    if plot:
        sns.countplot(x=dataframe[col_name], data = dataframe)
        plt.show(block=True)

cat_summary(df,"sex", plot=True)

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]


for col in cat_cols:
    if df[col].dtypes == "bool":
        print("asdasdasdasdas")
    else:
        cat_summary(df,col, plot=True )


df ["adult_male"].astype(int)

for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col,plot=True)
    else:
        cat_summary(df,col, plot=True)





def cat_summary(dataframe,col_name,plot=False):
    if dataframe[col_name].dtypes == "bool":
        dataframe[col_name] = dataframe[col_name].astype(int)

        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")


        if plot:
            sns.countplot(x=dataframe[col_name], data = dataframe)
            plt.show(block=True)
    else:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)

cat_summary(df, "adult_male", plot=True)






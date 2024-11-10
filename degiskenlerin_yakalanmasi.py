import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")
df.head()

#docstring

def grap_col_names(dataframe,cat_th=10, car_th=20):
    """
    veri setindek kategorik vs vs vs

    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe
    cat_th: int,float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int,float
        kategorik fakat kardinal değişkenler için sınıf eşik dğeri

    Returns
    -------
    cat_cols: list
        kategorik değişken listesi
    num_cols: list
        numerik dğeişken listesi
    cat_but_cat: list
        kategorik görüntülü kardinal değişken listesi

    Notes
    -----
    cat_cols + num_cols + cat_but_cat = toplam değişken sayısı
    num_but_cot cot_cols'un içerisinde
    return olan 3 liste toplam değişken sayısına eşittilr: cot_cols + num_cols + cat_but_cat

    """
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float", "bool"]]

    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols =  [col for col in df.columns if df[col].dtypes in ["int","float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observations: {dataframe.shape[1]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}")

    return cat_cols,num_cols,cat_but_car

cat_cols,num_cols,cat_but_car=grap_col_names(df)


def cat_summary(dataframe,col_name,plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

cat_summary(df,"sex")

for col in cat_cols:
    cat_summary(df,col)

def new_summary(dataframe,numerical_tool,plot=False):
    quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,0.95,0.99]
    print(dataframe[numerical_tool].describe(quantiles).T)

    if plot:
        dataframe[numerical_tool].hist()
        plt.xlabel(numerical_tool)
        plt.title(numerical_tool)
        plt.show(block=True)

for col in num_cols:
    new_summary(df,col,plot=True)



df = sns.load_dataset("titanic")
df.info()
for col in df.columns:
    if df[col].dtypes == "bool":
        df[col]= df[col].astype(int)

cat_cols,num_cols,cat_but_car=grap_col_names(df)


def cat_summary(dataframe,col_name,plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

for col in cat_cols:
    cat_summary(df,col,plot=True)








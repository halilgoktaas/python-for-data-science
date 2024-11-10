#list dict comprehension uygulamaları

#bir veri setindeki değişken isimlerini değiştirmek

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns
A = []
for col in df.columns:
    A.append(col.upper())

df = sns.load_dataset("car_crashes")
df.columns= [col.upper() for col in df.columns]
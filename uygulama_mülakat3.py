#amaç key'i string value'su aşağıdaki gibi string oluşturmak
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]
soz = {}
agg_list = ["mean","min","max","sum"]

for col in num_cols:
    soz[col] = agg_list

#kısa yolu
new_dict = {col: agg_list for col in num_cols}

df[num_cols].agg(new_dict)
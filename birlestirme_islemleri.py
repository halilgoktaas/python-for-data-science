import numpy as np
import pandas as pd
m = np.random.randint(1,30,size=(5,3))
df1= pd.DataFrame(m,columns= ["var1","var2","var3"])
df2= df1 + 99

pd.concat([df1,df2],ignore_index=True)

#marge ile birleştirme işlemleri



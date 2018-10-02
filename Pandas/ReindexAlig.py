import pandas as pd
import numpy as np

df1=pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2=pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])
print(df1)
print(df2)
df1=df1.reindex_like(df2)
print(df1)



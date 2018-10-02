import pandas as pd
import numpy as np
df1=pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2=pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
print(df1)
print(df2)
df2.reindex_like(df1)
#print(df1)
print("Data frame with forward fill")
print(df2.reindex_like(df1,method='ffill',limit=3))



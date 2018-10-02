import pandas as pd
import numpy as np
#creat dict of series
d={'Name':pd.Series(['Tina','Mina','Sina','Rina','Rita']),'Age':pd.Series([15,16,17,18,19]),'Rating':([1,2,3,4,5])}
df=pd.DataFrame(d)
print(df)
print(df.sum())# by default axis is 0 for sum(row wise)
print(df.sum(1))# took axis 1 which is coloumn
print(df.mean())#use of mean function
print(df.std(0))#standard deviation
print(df.describe(include=['object']))#computes a summary of statistics
print(df.describe(include='all'))#computes a summary of statistics


import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np

#加载数据
#备用地址：http://cdn.powerxing.com/files/lr-binary.csv
df = pd.read_csv("http://cdn.powerxing.com/files/lr-binary.csv")

#浏览数据集
print(df.head())
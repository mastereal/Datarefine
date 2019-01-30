import pandas as pd
from pandas import DataFrame, Series

AHflood_origin = pd.read_excel("./安徽洪涝.xlsx",header=3,sheet_name=0,index_col=0)
print(AHflood_origin)
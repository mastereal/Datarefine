import pandas as pd
from pandas import DataFrame, Series

ZJdrought=pd.read_excel("./ZJ_drought.xlsx",header=0,sheet_name=0,index_col=0,nrows=545).fillna(0).convert_objects(convert_numeric=True) # 用0填充NaN，且把数据变为整数类型

JXdrought=pd.read_excel("./JX_drought.xlsx",header=0,sheet_name=0,index_col=0,nrows=545).fillna(0).convert_objects(convert_numeric=True)

ZJdrought.to_excel("./BeforeRefine/ZJ_drought.xlsx")
JXdrought.to_excel("./BeforeRefine/JX_drought.xlsx")
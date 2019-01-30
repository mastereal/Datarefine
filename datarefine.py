import pandas as pd
from pandas import DataFrame, Series

AHflood_origin = pd.read_excel("./安徽洪涝.xlsx",header=3,sheet_name=0,index_col=0,nrows=545).fillna(0).convert_objects(convert_numeric=True) # 用0填充NaN，且把数据变为整数类型
#print(AHflood_origin)
AHflood_default=pd.read_excel("./AH_test_flood.xlsx",header=0,sheet_name=0,index_col=0).fillna(0).convert_objects(convert_numeric=True)
AHflood_origin.columns=AHflood_default.columns
AH_flood_o=AHflood_default+AHflood_origin
AH_flood=AH_flood_o.fillna(0)
#print(AH_flood)
AH_flood.to_excel("./AH_flood.xlsx")

AHdrought_origin = pd.read_excel("./安徽干旱.xlsx",header=3,sheet_name=0,index_col=0,nrows=545).fillna(0).convert_objects(convert_numeric=True) # 用0填充NaN，且把数据变为整数类型
#print(AHflood_origin)
AHdrought_default=pd.read_excel("./AH_test_drought.xlsx",header=0,sheet_name=0,index_col=0).fillna(0).convert_objects(convert_numeric=True)
AHdrought_origin.columns=AHdrought_default.columns
AH_drought_o=AHdrought_default+AHdrought_origin
AH_drought=AH_drought_o.fillna(0)
AH_drought.to_excel("./AH_drought.xlsx")

AHfreeze_origin = pd.read_excel("./安徽低温.xlsx",header=3,sheet_name=0,index_col=0,nrows=545).fillna(0).convert_objects(convert_numeric=True) # 用0填充NaN，且把数据变为整数类型
AHfreeze_default=pd.read_excel("./AH_test_freeze.xlsx",header=0,sheet_name=0,index_col=0).fillna(0).convert_objects(convert_numeric=True)
AHfreeze_origin.columns=AHfreeze_default.columns
AH_freeze_o=AHfreeze_default+AHfreeze_origin
AH_freeze=AH_freeze_o.fillna(0)
AH_freeze.to_excel("./AH_freeze.xlsx")

AHwind_origin = pd.read_excel("./安徽大风.xlsx",header=3,sheet_name=0,index_col=0,nrows=545).fillna(0).convert_objects(convert_numeric=True) # 用0填充NaN，且把数据变为整数类型
AHwind_default=pd.read_excel("./AH_test_wind.xlsx",header=0,sheet_name=0,index_col=0).fillna(0).convert_objects(convert_numeric=True)
AHwind_origin.columns=AHwind_default.columns
AH_wind_o=AHwind_default+AHwind_origin
AH_wind=AH_wind_o.fillna(0)
AH_wind.to_excel("./AH_wind.xlsx")

JXflood_origin = pd.read_excel("./江西洪涝.xlsx",header=3,sheet_name=0,index_col=0,nrows=545).fillna(0).convert_objects(convert_numeric=True) # 用0填充NaN，且把数据变为整数类型
JXflood_default=pd.read_excel("./JX_default.xlsx",header=0,sheet_name=0,index_col=0).fillna(0).convert_objects(convert_numeric=True)
JXflood_origin.columns=JXflood_default.columns
JX_flood_o=JXflood_default+JXflood_origin
JX_flood=JX_flood_o.fillna(0)
JX_flood.to_excel("./JX_flood.xlsx")

JXwind_origin = pd.read_excel("./江西大风.xlsx",header=3,sheet_name=0,index_col=0,nrows=545).fillna(0).convert_objects(convert_numeric=True) # 用0填充NaN，且把数据变为整数类型
JXwind_default=pd.read_excel("./JX_default.xlsx",header=0,sheet_name=0,index_col=0).fillna(0).convert_objects(convert_numeric=True)
JXwind_origin.columns=JXwind_default.columns
JX_wind_o=JXwind_default+JXwind_origin
JX_wind=JX_wind_o.fillna(0)
JX_wind.to_excel("./JX_wind.xlsx")

JXfreeze_origin = pd.read_excel("./江西低温.xlsx",header=3,sheet_name=0,index_col=0,nrows=545).fillna(0).convert_objects(convert_numeric=True) # 用0填充NaN，且把数据变为整数类型
JXfreeze_default=pd.read_excel("./JX_default.xlsx",header=0,sheet_name=0,index_col=0).fillna(0).convert_objects(convert_numeric=True)
JXfreeze_origin.columns=JXfreeze_default.columns
JX_freeze_o=JXfreeze_default+JXfreeze_origin
JX_freeze=JX_freeze_o.fillna(0)
JX_freeze.to_excel("./JX_freeze.xlsx")

ZJflood_origin = pd.read_excel("./浙江洪涝.xlsx",header=3,sheet_name=0,index_col=0,nrows=545).fillna(0).convert_objects(convert_numeric=True) # 用0填充NaN，且把数据变为整数类型
ZJflood_default=pd.read_excel("./ZJ_default.xlsx",header=0,sheet_name=0,index_col=0).fillna(0).convert_objects(convert_numeric=True)
ZJflood_origin.columns=ZJflood_default.columns
ZJ_flood_o=ZJflood_default+ZJflood_origin
ZJ_flood=ZJ_flood_o.fillna(0)
ZJ_flood.to_excel("./ZJ_flood.xlsx")


ZJwind_origin = pd.read_excel("./浙江大风.xlsx",header=3,sheet_name=0,index_col=0,nrows=545).fillna(0).convert_objects(convert_numeric=True) # 用0填充NaN，且把数据变为整数类型
ZJwind_default=pd.read_excel("./ZJ_default.xlsx",header=0,sheet_name=0,index_col=0).fillna(0).convert_objects(convert_numeric=True)
ZJwind_origin.columns=ZJwind_default.columns
ZJ_wind_o=ZJwind_default+ZJwind_origin
ZJ_wind=ZJ_wind_o.fillna(0)
ZJ_wind.to_excel("./ZJ_wind.xlsx")

ZJfreeze_origin = pd.read_excel("./浙江低温.xlsx",header=3,sheet_name=0,index_col=0,nrows=545).fillna(0).convert_objects(convert_numeric=True) # 用0填充NaN，且把数据变为整数类型
ZJfreeze_default=pd.read_excel("./ZJ_default.xlsx",header=0,sheet_name=0,index_col=0).fillna(0).convert_objects(convert_numeric=True)
ZJfreeze_origin.columns=ZJfreeze_default.columns
ZJ_freeze_o=ZJfreeze_default+ZJfreeze_origin
ZJ_freeze=ZJ_freeze_o.fillna(0)
ZJ_freeze.to_excel("./ZJ_freeze.xlsx")
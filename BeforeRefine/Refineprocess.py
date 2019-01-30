import os
import re
import pandas as pd
from pandas import DataFrame, Series

dirlist=os.listdir(path=".")
print(dirlist)
matchlist=["AH","JX","JS","ZJ"]
alist=range(1368,1913)
for pro in matchlist:
    filepath="./"+pro+".xlsx"
    protable=pd.read_excel(filepath,header=1,sheet_name=0,index_col=0)  
    prelist=list(protable.columns.str.strip()) #提取府名列表 stored in list
    #print(prelist)
    preindex=[]
    for pre in prelist:
        if re.match(r"Unnamed",pre)==None:
            i=prelist.index(pre)
            preindex.append(i)  # get index in the list of each prefecture, and store these index in another list
    print(preindex) # 获得了府名位置的列表，开始新的process
    
    a=re.compile(pro+"_")
    for filename in dirlist:
        if a.match(filename)!=None: #检查当前文件的文件名匹配
            filepath_match="./"+filename
            ori_data=pd.read_excel(filepath_match,header=0,sheet_name=0,index_col=0)  
            countylist=list(ori_data.columns.str.strip()) #提取县名列表 stored in list
            for in_num in preindex:
                i_1=preindex.index(in_num)+1 # 获取当前府和下一个府的索引号
                if i_1<len(preindex)-1:
                    in_num_1=preindex[i_1]
                    checklist=countylist[in_num:in_num_1] #获得当前府的县级列表
                    #print(checklist)
                    pre_c=countylist[in_num]
                    for year in alist:
                        i_year=alist.index(year)
                        if ori_data.iloc[i_year,in_num]!=0 and ori_data.iloc[i_year,in_num:in_num_1].sum()<2: #检查当前年份，当前府的数据
                            inpnum=in_num+1
                            inputlist=countylist[inpnum:in_num_1]
                            ori_data.iloc[i_year,inpnum:in_num_1]+=1 #完成当前年份，当前府的数据重新录入
                    # 循环结束，完成所有年份，当前府的数据重新录入
            #循环结束，完成所有府的数据重新录入
            outputpath="../AfterRefine/"+filename
            ori_data.to_excel(outputpath)
                    

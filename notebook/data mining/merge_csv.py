# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:58:58 2020

@author: a2aniket
"""

import pandas  as pd
from os import listdir
from os.path import isfile, join
import numpy as np

get_csv = [f for f in listdir("../../data/minied/Cap-1 Student info/") if isfile(join("../../data/minied/Cap-1 Student info/", f))]
#final_data=pd.DataFrame(columns=["Sr.No.","Merit No","Marks","Application ID","Name of Candidate","Gender","Category","PWD/DEF","Sub Group","Seat Type","Course","Collage"])
data=pd.read_csv("../../data/minied/Cap-1 Student info/student0201-1002.csv",converters={'Sr.No.':lambda x:str(x)})
new_columns=["Sr.No.","Merit No","Marks","Application ID","Name of Candidate","Gender","Category","PWD/DEF","Sub Group","Seat Type","cource_code","college_code"]
    
for file in get_csv:
    data2=pd.read_csv("../../data/minied/Cap-1 Student info/{}".format(file),converters={'Sr.No.':lambda x:str(x)})
    data=pd.concat([data[new_columns],data2[new_columns]], ignore_index=True)
        
    
data.to_csv("../../data/raw/Cap-1 Student Info.csv")
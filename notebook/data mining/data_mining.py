# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:32:22 2020

@author: a2aniket
"""
import pandas as pd
import camelot
from get_course_code import code
import os
import time

def mine_data(path,college):
    pdf=camelot.read_pdf(path,pages='all')
    length = pdf.__len__()
    college_code=college[0:4]
    columns=["Sr.No.","Merit No","Marks","Application ID","Name of Candidate","Gender","Category","PWD/DEF","Sub Group","Seat Type"]
    new_columns=["Sr.No.","Merit No","Marks","Application ID","Name of Candidate","Gender","Category","PWD/DEF","Sub Group","Seat Type","cource_code","college_code"]
    for i in range(0,length):
        shape=pdf[i].shape
        if shape[1] <= 2:
            course_path="../../data/minied/Cap-1 Cource/cource{}-{}.csv".format(college_code,i)
            pdf[i].to_csv(course_path)
            course_code=(code(course_path))
        else:
            student_deatil_path="../../data/minied/Cap-1 Student info/student{}-{}.csv".format(course_code,college_code)
            if os.path.exists(student_deatil_path):
                dataFrame=pd.read_csv(student_deatil_path)
                pdf[i].to_csv(student_deatil_path)
                new_dataFrame=pd.read_csv(student_deatil_path,names=columns,header=0)
                new_dataFrame["cource_code"]=course_code
                new_dataFrame["college_code"]=college_code
                dataFrame=pd.concat([dataFrame[new_columns],new_dataFrame[new_columns]],ignore_index=True)
                #dataFrame.append(new_dataFrame)
                dataFrame.to_csv(student_deatil_path)
            else:
                pdf[i].to_csv(student_deatil_path)
                dataFrame=pd.read_csv(student_deatil_path)
                dataFrame["cource_code"]=course_code
                dataFrame["college_code"]=college_code
                dataFrame.to_csv(student_deatil_path)
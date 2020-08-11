# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:08:28 2020

@author: sai
"""


import pandas as pd

dataframe=pd.read_csv("DSE data/table1.csv")
dataframe=dataframe.drop(["CAP I","CAP II","CAP III","Sr. No"],axis=1)
dataframe.to_csv("final data/college maping.csv")
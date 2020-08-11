# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:39:45 2020

@author: a2aniket
"""
import pandas as pd


def code(path):
    data=pd.read_csv(path)
    col=data.columns
    col=str(col).split()
    col=col[-2]
    code=col[0:4]
    return code



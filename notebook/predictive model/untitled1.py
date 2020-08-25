# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:07:39 2020

@author: sai
"""

import pickle
cast="SC.c"
dist="Pune"
path='../../data/Train Model/dist/Pune/model SC.c.pkl'
model = pickle.load(open(path, 'rb'))
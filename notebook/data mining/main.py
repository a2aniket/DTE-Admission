# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 05:41:33 2020

@author: a2aniket
"""


from os import listdir
from os.path import isfile, join
from data_mining import mine_data


#get all pdf fie from the folder
get_college = [f for f in listdir("../../data/source/cap1 AllotmentFinal/") if isfile(join("../../data/source/cap1 AllotmentFinal/", f))]


# mine the data from eatch pdf
for college in get_college:
    path="../../data/source/cap1 AllotmentFinal/{}".format(college)
    mine_data(path, college)
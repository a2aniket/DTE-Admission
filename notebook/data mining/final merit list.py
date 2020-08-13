# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 07:44:18 2020

@author: shubham
"""
import pandas as pd
import camelot
import os
import time

pdf=camelot.read_pdf("../../data/source/final merit list",pages=3)
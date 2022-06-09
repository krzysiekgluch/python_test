# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:32:00 2022

@author: N1400274
"""

import csv
import re


data = []
with open('c:/python/bazy/data.txt','rt') as f:
    data = csv.reader(f) 
    
    for row in data:
        print(row)
        x=re.split('\t| ',row[0])
        print(x[0])
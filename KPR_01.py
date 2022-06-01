# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:34:43 2022

@author: N1400274
"""

import os
import pandas as pd
import cx_Oracle

os.chdir("c:/python/bazy") # format:'C:/folder/folder'
file='p.txt'
line = open(file, "r").readlines()
userpwd=line[0]
       
connection = cx_Oracle.connect("N1400274", password=userpwd, dsn="KMB_PRE")  #<na produkcję dsn= KMB_PRD">
query = connection.cursor()

rs=query.execute("""SELECT max(start_dt) FROM kpr.cred_dim""")
df=pd.DataFrame(rs.fetchall())

col_names=[]
for i in range(0, len(query.description)):      
    col_names.append(query.description[i][0])

df.columns=col_names 
connection.close()    

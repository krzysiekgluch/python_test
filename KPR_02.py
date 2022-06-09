# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:34:43 2022

"""

#skrypt wykonuje zewnetrzny SQL na bazie oracle i mierzy czas

import os
import pandas as pd
import cx_Oracle
import time

os.chdir("c:/python/bazy") # format:'C:/folder/folder'
file='p.txt'

line = []
with open(file, "r") as file:
    line = file.readlines()

#with open as
userpwd=line[0]
       
connection = cx_Oracle.connect("N1400274", password=userpwd, dsn="KMB_PRE")  #<na produkcję dsn= KMB_PRD">
query = connection.cursor()


with open("c:/python/bazy/sql.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)

print(lines)
sql_text=[]

for i in lines:
    a=str(i)
    sql_text.append(a)
    
sql = ''.join(sql_text)

print(sql)

# rs=query.execute(sql)
rs=query.execute("select max(end_dt) as end_Dt, min(end_dt) as end_dt from kpr.cust_ent_dim \
                      union all \
                          select max(end_dt) as end_Dt, min(end_dt) as end_dt from kpr.cust_ent_dim ")
print("Fetching data: started")
start_time = time.time()
data=pd.DataFrame(rs.fetchall())
print("Fetching data: finished. time: {} s".format(time.time() - start_time))
print(len(query.description))
print(data)
col_names=[]
print(query.description)
for i in range(0, len(query.description)):
    col_names.append(query.description[i][0])
print(col_names)
print(data.columns)
data.columns=col_names
print(data)
connection.close()
end_time = time.time()
print (end_time - start_time)
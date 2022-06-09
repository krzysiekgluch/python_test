# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:38:21 2022

@author: N1400274
"""

# import os
import pyodbc
import pandas as pd
import time


#################
# SQL - odczyt
#################

with open("c:/python/bazy/sql_server_prokred_raporty.sql") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)

print(lines)
sql_text=[]

for i in lines:
    a=str(i)
    sql_text.append(a)
    
sql_command = ''.join(sql_text)

# Trusted Connection to Named Instance
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=mt1762sql2\mt1762sql2;DATABASE=PROKRED_DATA_TEST;Trusted_Connection=yes;')

#connection = pyodbc.connect(r'Driver=SQL Server;Server=.\mt1762sql2;Database=PROKRED_DATA_TEST;Trusted_Connection=yes;')
cursor = connection.cursor()
# cursor.execute("SELECT count(1) as ile  \
#               FROM [PROKRED_DATA_TEST].[dbo].[SDMO_podmiot];")

rs=cursor.execute(sql_command)
print("Fetching data: started")
start_time = time.time()
data=pd.DataFrame(rs.fetchall())`
print("Fetching data: finished. time: {} s".format(time.time() - start_time))
print(len(cursor.description))
print(data)

# zczytanie kolumn jako tutaj nie działą

# col_names=[]
# print(cursor.description)
# for i in range(0, len(cursor.description)):
#     col_names.append(cursor.description[i][0])
# print(col_names)
# print (data.columns)
# data.columns=col_names
# print(data)

connection.close()
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:38:21 2022

@author: N1400274
"""

import os
import pyodbc
import pandas as pd

# Trusted Connection to Named Instance
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=mt1762sql2\mt1762sql2;DATABASE=PROKRED_DATA_TEST;Trusted_Connection=yes;')

#connection = pyodbc.connect(r'Driver=SQL Server;Server=.\mt1762sql2;Database=PROKRED_DATA_TEST;Trusted_Connection=yes;')
cursor = connection.cursor()
# cursor.execute("SELECT count(1) as ile  \
#               FROM [PROKRED_DATA_TEST].[dbo].[SDMO_podmiot];")

cursor.execute("WITH BAZA AS \
                (SELECT count(1) over() AS ILE \
                		,[R_ID]\
                		,left(convert(varchar, [R_DATA_UTWORZENIA_RAPORTU], 120), 10) as [data_utworzenia]\
                		,reason.dii_name as  typ_raportu\
                		,RLV_PRODUCT_TYPE as typ\
                		,RLV_CONTRACT_ID\
                		,PDT_SYS_CENTRAL_ID as pid\
                		, PDT_NAZWA as nazwa\
                		, segment.dii_name as segment\
                		,left(segment.dii_name,2) as short_segment\
                		,DATALENGTH(R_WYGENEROWANY_DOKUMENT)/1024/1024 as rozmiar\
                		\
                  FROM [SDMO_REPORT]	inner join SDMO_REPORT_LOAN_SUMMARY_SPECIFICATION on R_LOAN_SUMMARY_SPECIFICATION = RLSS_ID\
                						INNER Join SDMO_REPORT_LOAN_VALUE RLV ON RLV_LOAN_SUMMARY_SPECIFICATION  = RLSS_ID\
                						left join dic_item reason on R_QUERY_REASON = reason.dii_id\
                						LEFT JOIN SDMO_PODMIOT on R_REL_PODMIOT_AKTUAL= PDT_ID\
                						left join dic_item segment on segment.dii_id = pdt_segment\
                						left join dic_item status on RLV_CURRENT_PAYMENTS_STATUS = status.dii_id \
                						left join dic_item rel_type on RLV_RELATIONSHIP_TYPE = rel_type.dii_id\
                						where 1=1	\
                 					\
                		\
                 							AND left(convert(varchar, [R_DATA_UTWORZENIA_RAPORTU], 120), 10) > '2019/12/31'\
                 							and RLV_CONTRACT_ID = 'BIK'\
                 							and RLV_PRODUCT_TYPE in \
                								(\
                								'Dyskonto weksli'\
                								,'Faktoring'\
                								,'Gwarancja bankowa'\
                								,'Karta kredytowa lub płatnicza, debetowa z limitem'\
                								,'Kredyt hipoteczny'\
                								,'Kredyt inwestycyjny'\
                								,'Kredyt obrotowy'\
                								,'Kredyt obrotowy rewolwingowy'\
                								,'Kredyt płatniczy w rachunku bieżącym'\
                								,'Kredyt w rachunku bieżącym'\
                								,'Kredyt w wyniku realizacji gwarancji/ poręczenia'\
                								,'Leasing'\
                								,'Linia kredytowa na otwieranie akredytyw'\
                								,'Nieuprawnione saldo debetowe'\
                								,'Poręczenie bankowe'\
                								)	\
                 							and (\
                 									(RLV_CLOSING_DATE is null or \
                 									left(convert(varchar, RLV_CLOSING_DATE, 120), 10) > '2021-10-13')\
                 									or status.dii_name like '%RESTRUKTURYZACJI%'\
                 									OR STATUS.dii_name like '%WINDYKACJI%'\
                 							\
                								)\
                                                 and r_id = 18165\
		) \
\
		select * from baza;")


data = cursor.fetchall()
print(data)
print(cursor.description)
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row.typ)
    
connection.close()
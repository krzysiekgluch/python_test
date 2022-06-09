WITH BAZA AS
(
SELECT  --top (100)
		count(1) over() AS ILE
		,[R_ID]
		--,[R_REL_PODMIOT_HIST]
		--,[R_REL_PODMIOT_AKTUAL]
		,left(convert(varchar, [R_DATA_UTWORZENIA_RAPORTU], 120), 10) as [data_utworzenia]
		,reason.dii_name as  typ_raportu
		--,[RLSS_CANCELLED_PRODUCTS_GUARANTOR]
		--,[RLSS_CANCELLED_PRODUCTS_HOLDER]
		--,[RLSS_COLLECTED_PRODUCTS_GUARANTOR]
		--,[RLSS_COLLECTED_PRODUCTS_HOLDER]
		,RLV_PRODUCT_TYPE as typ
		,RLV_CONTRACT_ID
		,PDT_SYS_CENTRAL_ID as pid
		, PDT_NAZWA as nazwa
		, segment.dii_name as segment
		,left(segment.dii_name,2) as short_segment
		,DATALENGTH(R_WYGENEROWANY_DOKUMENT)/1024/1024 as rozmiar
		
  FROM [SDMO_REPORT]	inner join SDMO_REPORT_LOAN_SUMMARY_SPECIFICATION on R_LOAN_SUMMARY_SPECIFICATION = RLSS_ID
						INNER Join SDMO_REPORT_LOAN_VALUE RLV ON RLV_LOAN_SUMMARY_SPECIFICATION  = RLSS_ID
						left join dic_item reason on R_QUERY_REASON = reason.dii_id
						LEFT JOIN SDMO_PODMIOT on R_REL_PODMIOT_AKTUAL= PDT_ID
						left join dic_item segment on segment.dii_id = pdt_segment
						left join dic_item status on RLV_CURRENT_PAYMENTS_STATUS = status.dii_id 
						left join dic_item rel_type on RLV_RELATIONSHIP_TYPE = rel_type.dii_id
						where 1=1	
						/*and RLV_PRODUCT_TYPE in (	'Biznes partner',
													'VAT0 PLN RACHUNEK VAT MSP TARYFA VAT MSP',
													'Rach.bie¿¹cy instytucjonalny',
													'VAT0 PLN RACHUNEK VAT TARYFA VAT KORPORACJA',
													'Rach.bie¿¹cy nasza wspólnota',
													'RACH.ŒR.WYODR.DOT.REALIZ.PROJ.',
													'RACHUNEK BIE¯¥CY NORDEA',
													'RACHUNEK VAT MSP',
													'RACHUNEK VAT KORPO',
													'DEPO T 020X05 RACHUNEK BIE¯¥CY BEZ DSD IR RLD',
													'RACHUNEK BIE¯¥CY POMOCNICZY',
													'RACHUNEK BIE¯¥CY DE',
													'RACH.POMOCNICZY MSP',
													'Rach.bie¿.rynku mieszkaniowego',
													'RACHUNEK BIE¯¥CY CZ',
													'RACH.WYODRÊBNIONYCH WP£YWÓW',
													'RACHUNEK INTELIGO FIRMOWY',
													'RACHUNEK BIE¯¥CY ADM',
													'RACHUNEK BIE¯¥CY ADM.',
													'RACHUNEK WINDYK. NORDEA',
													'RACHUNEK W UPAD£OŒCI NORDEA ',
													'RACHUNEK DLA FIRM ADM.',
													'RACHUNEK DLA FIRM PLUS ADM.',
													'RACHUNEK BIE¯¥CY DLA MIŒ',
													'RACHUNEK INTELIGO FIRMOWY NSD',
													'RACHUNEK BIE¯¥CY SK',
													'RACHUNEK POWIERNICZY',
													'RACH.BIE¯¥CY DLA LOKACYJNEGO')*/
		
							AND left(convert(varchar, [R_DATA_UTWORZENIA_RAPORTU], 120), 10) > '2019/12/31'
							and RLV_CONTRACT_ID = 'BIK'
							and RLV_PRODUCT_TYPE in 
								(
								'Dyskonto weksli'
								,'Faktoring'
								,'Gwarancja bankowa'
								,'Karta kredytowa lub p³atnicza, debetowa z limitem'
								,'Kredyt hipoteczny'
								,'Kredyt inwestycyjny'
								--Kredyt na zakup papierów wartoœciowych
								,'Kredyt obrotowy'
								,'Kredyt obrotowy rewolwingowy'
								,'Kredyt p³atniczy w rachunku bie¿¹cym'
								,'Kredyt w rachunku bie¿¹cym'
								,'Kredyt w wyniku realizacji gwarancji/ porêczenia'
								,'Leasing'
								,'Linia kredytowa na otwieranie akredytyw'
								,'Nieuprawnione saldo debetowe'
								,'Porêczenie bankowe'
								)	
							and (
									(RLV_CLOSING_DATE is null or 
									left(convert(varchar, RLV_CLOSING_DATE, 120), 10) > '2021-10-13')
									or status.dii_name like '%RESTRUKTURYZACJI%'
									OR STATUS.dii_name like '%WINDYKACJI%'
							
								)
							and r_id = 18165
							--and (
							--	segment.dii_name like '13%'
							--	or segment.dii_name like '45%'

							--	or segment.dii_name like '14%')
		) 

		select * from baza
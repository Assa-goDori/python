'''
Created on 2020. 8. 19.

@author: GDJ24
0819/exam3.py : 컬럼만 선택하기
                sales_2013.xlsx 파일의 january_2013 sheet의 열이 
                "Customer Name","Sale Amount" 컬럼만 
                sales_2013_amt.xlsx 파일로 저장하기
'''
import pandas as pd

infile = "../0818/sales_2013.xlsx"
outfile = "sales_2013_amt.xlsx"
df = pd.read_excel(infile,'january_2013',index_col=None)
df_value = df.loc[:,['Customer Name','Sale Amount']]
writer = pd.ExcelWriter(outfile)
df_value.to_excel(writer,sheet_name="jan_2013",index=False)
writer.save()


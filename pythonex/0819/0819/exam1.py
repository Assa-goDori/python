'''
Created on 2020. 8. 19.

@author: GDJ24
0819/exam1.py : sale_2015.xlsx 파일중 Customer Name 컬럼의 값이 J로 시작하는 행만 선택하여 Sales_2015_J.xlsx 파일로 생성하기
'''
import pandas as pd

infile = "../0818/sales_2015.xlsx"
outfile = "Sales_2015_J.xlsx"
df = pd.read_excel(infile,'january_2015',index_col=None)
df_value = df[df["Customer Name"].str.startswith('J')]
writer = pd.ExcelWriter(outfile,engine="openpyxl")
df_value.to_excel(writer,sheet_name="sale_2015J",index=False)
writer.save()

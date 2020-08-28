'''
Created on 2020. 8. 19.

@author: GDJ24
0819/exam2.py : sale_2013.xlsx 파일중 
                Purchase Date 컬럼의 값이 "01/24/2013" 과 "01/31/2013" 인 행만 
                sales_2013_01.xlsx 파일로 저장하기
'''
import pandas as pd

infile = "../0818/sales_2013.xlsx"
outfile = "sales_2013_01.xlsx"
# df: sales_2013.xlsx 파일의 january_2013이름의 sheet 데이터를 DataFrame 의 타입으로 저장
indata =["01/24/2013","01/31/2013"]
# df_value : df 데이터중, 컬럼의 이름이 Purchase Date 인 값중 
        #    select_date 에 속한 값을 포함하는 행을 저장
#             df['Purchase Date'].isin(indata) 의 결과가 True 인 경우
df = pd.read_excel(infile,'january_2013',index_col=None)
df_value = df[df['Purchase Date'].isin(indata)]
print(df_value)
writer = pd.ExcelWriter(outfile,engine="openpyxl")
df_value.to_excel(writer,sheet_name="jan_13_output",index=False)
writer.save()

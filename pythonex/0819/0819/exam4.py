'''
Created on 2020. 8. 19.

@author: GDJ24
0819/exam4.py : 컬럼만 선택하기
                sales_2013.xlsx 파일의 모든  sheet 열이 "Customer Name", "Sale Amount" 컬럼만 
                sales_2013_allamt.xlsx 파일로 저장하기
'''
import pandas as pd
import glob # 경로명 표현시 사용되는 모듈
import os #시스템 관련된 모듈

inpath = "D:/uddone/python/workspace/pythonex/excel/"
outfile = "sales_all.xlsx"
# "*.xlsx : inpath 폴더의 모든 xlsx 파일 선택
# "*.xls* : inpath 폴더의 확장자가 xls로 시작하는 모든 파일 선택
excels = glob.glob(os.path.join(inpath,"*.xlsx"))
rows = [] #DateFrame 객체를 리스트로 저장하는 객체
for excel in excels :
    print(excel)
    dfs = pd.read_excel(excel,sheet_name=None,index_col=None)
    for sheet_name,df in dfs.items() :
        rows.append(df)
# excel 파일로 저장
# axis=0  : row추가
#df_concat : 지정된 폴더에 있는 엑셀 파일의 모든 sheet의 데이터를 저장
#            row형태로 추가됨
df_concat = pd.concat\
                (rows,sort=False,axis=0,ignore_index=True)
print(type(df_concat))
writer = pd.ExcelWriter(outfile)
df_concat.to_excel\
    (writer,sheet_name="all_data_all_worksheet",index=False)
writer.save()
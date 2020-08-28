'''
Created on 2020. 8. 14.

@author: GDJ24
pandasex3.py : pandas를 이용하여 csv 파일 읽기2
'''
import pandas as pd

infile ="supplier_data.csv"
outfile = "pandas_out3.csv"
# read_csv : csv파일을 dataFrame 객체로 리턴
df = pd.read_csv(infile)
print(df)

importDate =["1/20/14","1/30/14"]
'''
    부분 DataFrame 객체 생성
    Purchase Date 열의 값 중 importDate 속한 모든 컬럼(제일 끝 ':' 로 표시) 조회
'''
df_inset = df.loc[df["Purchase Date"].isin(importDate),:]
print(df_inset)
print(type(df_inset))

#to_csv : DataFrame 객체를 csv 파일로 출력
#index=False : index정보 저장 X
df_inset.to_csv(outfile,index=False)
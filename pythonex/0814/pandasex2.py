'''
Created on 2020. 8. 14.

@author: GDJ24
pandasex2.py : pandas를 이용하여 csv 파일 읽기
'''
import pandas as pd

infile ="CCTV_guro.csv"
outfile = "pandas_out2.csv"
# 제일 윗단을 컬럼명으로 지정해준다.
df = pd.read_csv(infile)
print(df)

print(df["위도"])
'''
Created on 2020. 8. 19.

@author: GDJ24
0819/excelex7.py : pandas를 이용하여 xlsx 파일 읽기
                                출력되는  excel 파일의 sheet를 여러개로 저장하기
'''
import pandas as pd

infile = "../0818/ssec1804.xls"
outfile = "ssec1804_bak.xls"
writer = pd.ExcelWriter(outfile) #출력 파일을 설정
df = pd.read_excel(infile, sheet_name=None, index_col=None)
for worksheet_name,data in df.items() :
    print("===",worksheet_name,"===")
    print(data)
    #excel 파일에 sheet 저장
    data.to_excel \
    (writer,sheet_name = worksheet_name,index=False,header=False)
writer.save()
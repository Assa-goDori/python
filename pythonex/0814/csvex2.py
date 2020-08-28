'''
Created on 2020. 8. 14.

@author: GDJ24
csvex2.py : codecs 모듈을 이용하여 csv 파일 읽기
'''
import codecs
filename = "../0813/cctv3.csv"
csv = codecs.open(filename, "r", "euc-kr").read()   #코덱을 통해 한줄씩이 아니라 한번에 읽기
print(type(csv))
data = []
rows = csv.split("\r\n")
for row in rows :
    if row == "" : continue
    cells = row.split(",")
    data.append(cells)
outfp = open("cctv.txt", "w", encoding="UTF8")
for c in data :
#    print(c[0],c[1],c[2],c[3])
    outfp.write(" ".join(map(str,c)) + "\n")
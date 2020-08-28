'''
Created on 2020. 8. 13.

@author: GDJ24
csvex1.py : csv 파일 읽기.
            command 라인에서 입력 파일을 입력받기

cctv.csv : UTF8
cctv3.csv : EUC-KR 기본 인코딩
'''
import sys
#자바 : java MyApp 홍 김 : 홍 : args[0], 김 : args[1]
#C : MyApp.exe 홍 김 : MyApp.exe : argv[0], 홍 : argv[1], 김 : argv[2]

#파이썬 : D:\20200224\python\workspace\pythonex\0813\csvex1.py cctv.csv cctv2.csv : 경로 : argv[0], cctv.csv : argv[1], cctv2.csv : argv[2]
print(sys.argv[0], sys.argv[1], sys.argv[2])
infile = sys.argv[1]    #cctv.csv
outfile = sys.argv[2]   #cctv2.csv
with open(infile,"r",newline="") as filereader :
    with open(outfile,"w",newline="") as filewriter :
        header = filereader.readline()
        print(type(header))
        headlist = header.split(",")
        filewriter.write(",".join(map(str,headlist)) + "\r\n")
        for rowlist in filereader : 
            filewriter.write(rowlist)
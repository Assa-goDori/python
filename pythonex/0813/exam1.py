'''
Created on 2020. 8. 13.

@author: GDJ24
exam1.py : regularex3.py 파일을 읽어서 regularex3.bak 파일로 복사하기
'''

infp = None
outfp = None
outfp = open("regularex3.bak","w",encoding="UTF8")
inStr = ""
infp = open("../0813/regularex3.py", "r+", encoding="UTF8")
while True :
    inStr = infp.readline()
    if not inStr :  #EOF
        break
    outfp.writelines(inStr + "\n")
infp.close()
outfp.close()
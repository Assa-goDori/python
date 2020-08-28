'''
Created on 2020. 8. 13.

@author: GDJ24
fileex1.py : 파일 읽기
    open("파일이름","모드",인코딩방식)
        파일모드
        "r" : 읽기모드
        "w" : 쓰기모드
        "r+" : 읽기/쓰기모드
        "a" : 쓰기모드, 기존의 파일이 있는 경우 내용이 추가됨
        "t" : Text 모드. 문자형. 생략가능. 기본형.
        "b" : Binary 모드. 이진형(바이트형).
'''

infp = None
inStr = ""
infp = open("../0813/regularex3.py", "rt", encoding='UTF8')
while True :
    inStr = infp.readline()
    if not inStr :  #EOF(End Of File)
        break
    print(inStr, end="")
infp.close()
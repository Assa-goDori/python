'''
Created on 2020. 8. 12.

@author: GDJ24
regularex2.py : 정규식 사용하기
    {갯수} : 갯수
    \d : 숫자
    (\d{6,7})[-]\d{7} :
                첫번째 그룹 : 숫자 6자리 또는 7자리 + 문자 '-' + 숫자7자리
    \g<1> : 지정한 첫번째 그룹
    
    ? : 0 또는 1개
    ex) ca?t : a 문자가 없거나 1개인 경우
        "ct" : True
        "cat" : True
        "caaaaaat" : False
    * : 0개 이상
    ex) ca*t : a 문자가 0개 이상인 경우
        "ct" : True
        "cat" : True
        "caaaaaat" : True
    + : 1개 이상
    ex) ca+t : a 문자가 1개 이상인 경우
        "ct" : False
        "cat" : True
        "caaaaaat" : True
    {n} : n개 반복
    ex) ca{2}t : a 문자가 2개
        "ct" : False
        "cat" : False
        "caat" : True
        "caaaaaat" : False
    {n,m} : n개이상 m개 이하
    ex) ca{2,5}t : a 문자가 2개이상 5개 이하
        "ct" : False
        "cat" : False
        "caat" : True
        "caaaaat" : True
    
'''
import re   #정규식 사용을 위한 모듈

data = '''
    park 800805-1234567
    kim 800905-2345678
    choi 750905-a123456
'''
'''
re.compile(pattern) : pattern에 맞는 문자열을 지정
'''
pat = re.compile("(\d{6,7})[-]\d{7}")   #\d{6,7} : 앞쪽 6,7개의 숫자.  [-] : 하이픈 여부    \d{7} : 뒤쪽 7개 숫자
print(pat.sub("\g<1>-*******",data))    #g<1> : group을 의미. 위의 (\d{6,7}). 괄호 안에 있는 데이터=> 그룹.
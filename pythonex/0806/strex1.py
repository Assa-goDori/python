'''
Created on 2020. 8. 6.

@author: GDJ24
strex1.py : 문자열 처리. 문자열을 배열로 처리 가능함.
'''
print("안녕하세요")
print("안녕하세요"[0])   #안
print("안녕하세요"[4])   #요
print("안녕하세요"[-1])  #뒤부터 인덱스. 요
print("안녕하세요"[-2])  #뒤부터 인덱스. 세

#부분문자열
print("안녕하세요"[1:3]) #1번인덱스 부터 2번인덱스까지 부분 문자열. 녕하
print("안녕하세요"[:3]) #처음 부터 2번인덱스까지 부분 문자열. 안녕하
print("안녕하세요"[3:]) #3번인덱스부터 끝까지 부분 문자열. 세요
print("안녕하세요"[::2]) #0번 인덱스부터 2칸씩 부분 문자열 처리. 안하요
print("안녕하세요"[::-1]) #역순 출력. 요세하녕안
print("안녕하세요"[::-2]) #뒤부터 2칸 역순 출력. 요하안

#함수
print(type("안녕하세요")) #자료형 출력
print(len("안녕하세요")) #문자열 길이

a="hello"
cnt = 0;
# 'l' 문자의 갯수 출력하기(방법 1)
for i in range(0, len(a)) :
    if(a[i] == 'l') :
        cnt += 1
print("l문자의 갯수 : ",cnt)
# 'l' 문자의 갯수 출력하기(방법 2)
print("l문자의 갯수 : ", a.count('l'))

#문자 위치 출력. find vs index
# find : 없는 경우 -1 출력. index : 없는 경우 오류 발생
print("l문자의 위치 : ", a.find('l'))
print("a문자의 위치 : ", a.find('a'))
print("l문자의 위치 : ", a.index('l'))
print("a문자의 위치 : ", a.index('a'))
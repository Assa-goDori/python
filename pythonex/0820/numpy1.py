'''
Created on 2020. 8. 20.

@author: GDJ24
'''
import numpy as np

#수치 리스트 생성하기
print(np.array([1,4,2,5,3]))        #리스트의 값을 배열로
print(np.array([3.14,4,2,3]))       #리스트의 값을 실수형 배열
print(np.array([1,2,3,4], dtype='float32')) #실수형 배열

#기본 함수
# zeros : 0의 값을 가진 배열
arr = np.zeros(10, dtype=int)   #10개의 요소를 0으로 채움
print(arr)
print(type(arr))
#ones : 1의 값을 가진 배열
arr = np.ones((3,5), dtype=float)   #3행5열 실수형 배열 생성. 1로채움
print(arr)
#full : 지정된 값으로 배열의 값을 설정

arr = np.full((3,5),3.14) #3행 5열 리스트 생성. 3.14로 채움
print(arr)

#0~20 까지의 수를 2씩 증가시킨 값을 배열로 생성
arr = np.arange(0,21,2)
print(arr)

#0과 1사이의 일정한 간격의 5개의 값을 가진 배열 생성
arr = np.linspace(0,21,2)
print(arr)

#평균 0, 표준편차 1인 정규 분포를 따르는 3행3열 난수 배열 생성
arr = np.random.normal(0,1,(3,3))
print(arr)

#0~10 구간의 임의의 정수를 가진 3행 3열 배열 생성
arr = np.random.randint(0, 10, (3,3))
print(arr)

print(arr.ndim) # 배열의 차원
print(arr.shape)
print(arr.size) # 요소의 갯수
print(arr.dtype) # 요소의 자료형
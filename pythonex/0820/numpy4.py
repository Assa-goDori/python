'''
Created on 2020. 8. 20.

@author: GDJ24
numpy4.py : 배열의 연결 및 분할
'''
import numpy as np
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[3,2,1],[6,5,4]])
print(x)
print(y)
#배열의 연결
print(np.concatenate([x,y], axis=0))    #행으로 연결 : 수직연결
print(np.concatenate([x,y], axis=1))    #열로 연결 : 수평연결

#형태가 다른 배열의 연결
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[3,2,1],[6,5,4],[3,2,1]])
z = np.array([[7],[10]])
print(np.vstack([x,y])) #수직 기준, 행 기준 => 열의 값이 같아야함
print(np.hstack([x,z])) #수평 기준, 열 기준 => 행의 값이 동일해야 함
#print(np.vstack([x,z]))    #열의 값이 동일해야함. 오류발생.
#print(np.hstack([y,z]))    #행의 값이 동일해야함. 오류발생.

#배열의 분리
#0~15까지의 값을 4행4열 배열로 재배치하기
x = np.arange(16).reshape((4,4))
print(x)
upper, lower = np.vsplit(x,[2])     #2행을 기준으로 분리
print(upper)
print(lower)
left, right = np.hsplit(x, [2])     #2열을 기준으로 분리
print(left)
print(right)
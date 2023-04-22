import sys
from collections import *
def input():return sys.stdin.readline().rstrip()
N,K,P,X=map(int,input().split())
op=[63,6,91,79,102,109,125,7,127,111]
X=deque(str(X))
res=0
for i in range(1,N+1):
    num=deque(str(i))
    cnt=0
    while len(num)<len(X):
        num.appendleft('0')
    while len(num)>len(X):
       X.appendleft('0')
    for j in range(len(X)):
        cnt+=bin(op[int(num[j])]^op[int(X[j])])[2:].count('1')
        if cnt>P:break
    if 1<=cnt<=P:
        res+=1
print(res)
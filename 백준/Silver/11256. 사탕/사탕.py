import sys
from collections import *
def input(): return sys.stdin.readline().rstrip()
T=int(input())
while T:
    T-=1
    N,M=map(int,input().split())
    m=0
    arr=[]
    for i in range(M):
        a,b=map(int,input().split())
        arr.append(a*b)
    arr.sort(reverse=True)
    arr=deque(arr)
    res=0
    while N>0:
        N-=arr.popleft()
        res+=1
    print(res)
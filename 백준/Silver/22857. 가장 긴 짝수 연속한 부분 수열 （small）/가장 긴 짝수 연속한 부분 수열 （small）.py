import heapq
import itertools
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
dx=[0,1,0,-1,-1,-1,1,1]
dy=[1,0,-1,0,-1,1,1,-1]
N,M=map(int,input().split())
a=list(map(int,input().split()))
left=0
right=1
cnt=0
if a[0]&1:
    cnt+=1
res=1-cnt
while right<N:
    if a[right]&1:
        cnt+=1
    right+=1
    while cnt>M:
        if a[left]&1:
            cnt-=1
        left+=1
    res=max(res,right-left-cnt)
print(res)



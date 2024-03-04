import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
import copy
from collections import *
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N,K=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
b=[int(input()) for _ in range(K)]
b.sort()
a.sort()
q=[]
idx=0
res=0
for cur in b:
    while idx<N and cur>=a[idx][0]:
        heapq.heappush(q,-a[idx][1])
        idx+=1
    if q:
        res+=heapq.heappop(q)
    
print(-res)
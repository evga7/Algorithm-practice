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
N=int(input())
q=[]
a=[list(map(int,input().split())) for _ in range(N)]
a.sort(key=lambda x:x[1])
for cost,day in a:
    if len(q)<day:
        heapq.heappush(q,cost)
    else:
        if q[0]<cost:
            heapq.heappop(q)
            heapq.heappush(q,cost)
res=0
while q:
    res+=q.pop()
print(res)

import heapq
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import copy
from collections import *
import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
a.sort(key=lambda x:x[1])
res=0
q=[]
idx=0
for cur in a:
    cost,day=cur[0],cur[1]
    if len(q)<day:
        heapq.heappush(q,cost)
    else:
        if q[0]<cost:
            heapq.heappop(q)
            heapq.heappush(q,cost)
while q:
    res+=q.pop()

print(res)
import bisect
import heapq
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
a.sort()
res=0
q=[]
cnt=0
for cur in a:
    if cnt<cur[0]:
        heapq.heappush(q,cur[1])
        cnt+=1
    else:
        if q[0]<cur[1]:
            heapq.heappop(q)
            heapq.heappush(q,cur[1])
while q:
    res+=q.pop()
print(res)

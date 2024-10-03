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
N,M=map(int,input().split())
q=deque()
m=defaultdict(int)
q.append((0,N))

while q:
    cost,cur=q.popleft()
    if cur==M:
        print(cost)
        break
    for nxt in [cur*2,cur+1,cur-1]:
        if 0<=nxt<=100000 and not nxt in m:
            m[nxt]=cur
            q.append((cost+1,nxt))
v=[]
while M!=N:
    v.append(M)
    M=m[M]
v.append(N)
for i in range(len(v)-1,-1,-1):
    print(v[i],end=' ')

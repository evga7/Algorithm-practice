import heapq
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
a=list(map(int,input().split()))
q=deque()
c=[0 for _ in range(N+1)]
q.append(0)
c[0]=1
while q:
    cur=q.popleft()
    if cur==N-1:
        print("YES")
        exit(0)
    for i in range(cur+1,N):
        n_cost=(i-cur)*(1+abs(a[cur]-a[i]))
        if not c[i] and n_cost<=M:
            q.append(i)
            c[i]=1
print("NO")

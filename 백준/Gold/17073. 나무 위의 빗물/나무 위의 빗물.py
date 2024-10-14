from collections import *
import bisect
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
g=defaultdict(list)
for i in range(N-1):
    q,w=map(int,input().split())
    g[q].append(w)
    g[w].append(q)
cnt=0
for i in range(2,N+1):
    if len(g[i])==1:
        cnt+=1
print(M/cnt)
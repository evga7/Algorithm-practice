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
g=defaultdict(list)
dp=[[0 for _ in range(2)] for _ in range(N+1)]
visited=[0 for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
def go(cur):
    dp[cur][1]=1
    visited[cur]=1
    for nxt in g[cur]:
        if visited[nxt]:continue
        go(nxt)
        dp[cur][1]+=min(dp[nxt][1],dp[nxt][0])
        dp[cur][0]+=dp[nxt][1]
go(1)
print(min(dp[1]))

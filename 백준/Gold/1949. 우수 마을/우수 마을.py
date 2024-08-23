from collections import *
import bisect
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
a=list(map(int,input().split()))
g=defaultdict(list)
dp=[[0 for _ in range(2)] for _ in range(N+1)]
visited=[0 for _ in range(N+1)]
for i in range(N-1):
    q,w=map(int,input().split())
    g[q].append(w)
    g[w].append(q)
def go(cur):
    visited[cur]=1
    dp[cur][1]=a[cur-1]
    for nxt in g[cur]:
        if visited[nxt]:continue
        go(nxt)
        dp[cur][0]+=max(dp[nxt])
        dp[cur][1]+=dp[nxt][0]

go(1)
print(max(dp[1]))
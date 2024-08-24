from collections import *
import bisect
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
g=defaultdict(list)
g2=defaultdict(list)
dp=[[0 for _ in range(N+1)] for _ in range(2)]
visited=[0 for _ in range(N+1)]
for i in range(N-1):
    q,w=map(int,input().split())
    g[q].append(w)
    g[w].append(q)

def go(cur):
    visited[cur]=1
    dp[0][cur]=1
    for nxt in g[cur]:
        if visited[nxt]:continue
        go(nxt)
        dp[1][cur]+=dp[0][nxt]
        dp[0][cur]+=min(dp[0][nxt],dp[1][nxt])

go(1)
print(min(dp[0][1],dp[1][1]))
from collections import *
import bisect
import sys
sys.setrecursionlimit(10**8)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
g=defaultdict(list)
g2=defaultdict(list)
dp=[[-1 for _ in range(N+1)] for _ in range(2)]
visited=[0 for _ in range(N+1)]
for i in range(N-1):
    q,w=map(int,input().split())
    g[q].append(w)
    g[w].append(q)

def go(op,cur):
    if dp[op][cur]!=-1:
        return dp[op][cur]
    ret=987654321
    cnt=0
    if op:
        for nxt in g2[cur]:
            cnt+=go(0,nxt)
        ret=min(ret,cnt)
    cnt=1
    for nxt in g2[cur]:
        cnt+=go(1,nxt)
    ret = min(ret, cnt)
    dp[op][cur] = ret
    return dp[op][cur]
def go2(cur):
    visited[cur]=1
    for nxt in g[cur]:
        if visited[nxt]:continue
        g2[cur].append(nxt)
        go2(nxt)
go2(1)
print(min(go(0,1),go(1,1)))
import sys
sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
g=[[] for _ in range(N+1)]
a=list(map(int,input().split()))
p=list(map(int,input().split()))
dp=[[-1 for _ in range(2)] for _ in range(N+1)]
for i,cur in enumerate(a):
    g[cur].append(i+2)
def go(cur,f):
    if dp[cur][f]!=-1:
        return dp[cur][f]
    ret=0
    if f:
        for nxt in g[cur]:
            ret+=go(nxt,0)
    else:
        notmenti=0
        for nxt in g[cur]:
            notmenti+=go(nxt,0)
        menti=0
        for nxt in g[cur]:
            menti=(notmenti-go(nxt,0))+(go(nxt,1)+(p[cur-1]*p[nxt-1]))
            ret=max(ret,notmenti,menti)
    dp[cur][f]=ret
    return dp[cur][f]
    
print(go(1,0))    
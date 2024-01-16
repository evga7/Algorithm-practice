import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
dp=[[-1 for _ in range(1<<16)] for _ in range(N+1)]
def go(cur,bit):
    if bit==(1<<N)-1 and cur==0:
        return 0
    if dp[cur][bit]!=-1:
        return dp[cur][bit]
    ret=987654321
    for i in range(N):
        if cur!=i and not bit & (1<<i) and a[cur][i]:
            ret=min(ret,go(i,bit|(1<<i))+a[cur][i])
    dp[cur][bit]=ret
    return dp[cur][bit]
print(go(0,0))
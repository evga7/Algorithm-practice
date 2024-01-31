import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
# map(int,input().split())
INF = sys.maxsize
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
dp=[[-1 for _ in range(M+1)] for _ in range(N+1)]
def go(idx,w):
    if idx==N:
        return 0
    if dp[idx][w]!=-1:
        return dp[idx][w]
    ret=0
    b,c=a[idx][0],a[idx][1]
    if w+b<=M:
        ret=max(ret,go(idx+1,w+b)+c)
    ret=max(ret,go(idx+1,w))
    dp[idx][w]=ret
    return dp[idx][w]
print(go(0,0))


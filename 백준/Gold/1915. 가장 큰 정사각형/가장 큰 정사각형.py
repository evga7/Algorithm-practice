import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(map(int,input())) for _ in range(N)]
dp=[[-1 for _ in range(M+1)] for _ in range(N+1)]
def go(x,y):
    if x>=N or y>=M:
        return 0
    if not a[x][y]:
        return 0
    if dp[x][y]!=-1:
        return dp[x][y]
    ret=1
    ret=min(go(x,y+1),go(x+1,y),go(x+1,y+1))+1
    dp[x][y]=ret
    return dp[x][y]
res=0
for i in range(N):
    for j in range(M):
        if a[i][j]:
            res=max(res,go(i,j))
print(res*res)
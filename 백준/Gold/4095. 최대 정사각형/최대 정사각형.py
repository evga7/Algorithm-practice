import sys
sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
def go(x,y):
    if x>=N or y>=M:
        return 0
    if a[x][y]==0:
        return 0
    if dp[x][y]!=-1:
        return dp[x][y]
    ret=1
    ret=max(ret,min(go(x+1,y),go(x,y+1),go(x+1,y+1))+1)
    dp[x][y]=ret
    return dp[x][y]
while True:
    N, M = map(int, input().split())
    if not N and not M:
        break
    a = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-1 for _ in range(M)] for _ in range(N)]
    res=0
    for i in range(N):
        for j in range(M):
            if a[i][j]:
                res=max(res,go(i,j))
    print(res)
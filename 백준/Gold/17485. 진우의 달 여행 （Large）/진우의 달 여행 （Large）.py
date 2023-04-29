import sys
def input():return sys.stdin.readline().rstrip()
dy=[-1,0,1]
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
dp=[[[-1 for _ in range(4)] for _ in range(M)]for _ in range(N)]
def go(x,y,op):
    if x==N:
        return 0
    if dp[x][y][op]!=-1:
        return dp[x][y][op]
    ret=987654321
    for i in range(3):
        if op==i:continue
        n_y=y+dy[i]
        if 0<=n_y<M:
            ret=min(ret,go(x+1,n_y,i)+a[x][y])
    dp[x][y][op]=ret
    return dp[x][y][op]

res=987654321
for i in range(M):
    res=min(res,go(0,i,3))
print(res)
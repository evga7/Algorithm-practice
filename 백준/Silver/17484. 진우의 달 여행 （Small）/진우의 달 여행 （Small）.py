import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
dp=[[[-1 for _ in range(4)] for _ in range(M)] for _ in range(N)]
res=987654321
dy=[-1,0,1]
def go(x,y,dir):
    if x==N:
        return 0
    if dp[x][y][dir]!=-1:
        return dp[x][y][dir]
    ret=987564321
    for i in range(3):
        n_y=y+dy[i]
        if 0<=n_y<M:
            if dir==i:continue
            ret=min(ret,go(x+1,n_y,i)+a[x][y])
    dp[x][y][dir]=ret
    return dp[x][y][dir]

for i in range(M):
    res=min(res,go(0,i,3))
print(res)
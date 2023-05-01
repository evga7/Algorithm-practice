import sys
def input():return sys.stdin.readline().rstrip()
def is_inside(x,y):
    return 0<=x<N and 0<=y<M
N,M,K=map(int,input().split())
dp=[[[-1 for _ in range(301)] for _ in range(301)] for _ in range(101)]
a=[list(map(int,input().split())) for _ in range(N)]
def go(idx,x,y):
    if idx==N:
        return 0
    if x==M and y==K:
        return 0
    if dp[idx][x][y]!=-1:
        return dp[idx][x][y]
    ret=0
    if x+a[idx][0]<=M and y+a[idx][1]<=K:
        ret=max(ret,go(idx+1,x+a[idx][0],y+a[idx][1])+1)
    ret=max(ret,go(idx+1,x,y))
    dp[idx][x][y]=ret
    return dp[idx][x][y]

print(go(0,0,0))
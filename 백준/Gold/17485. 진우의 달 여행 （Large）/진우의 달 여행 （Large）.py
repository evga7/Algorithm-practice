import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
dp=[[[-1 for _ in range(4)] for _ in range(M+1)] for _ in range(N+1)]
def go(x,y,op):
    if x==N:
        return 0
    if dp[x][y][op]!=-1:
        return dp[x][y][op]
    ret=987654321
    for i in range(3):
        n_x=x+1
        n_y=y+dy[i]
        if op==i:continue
        if is_inside(n_x,n_y,N+1,M):
            ret=min(ret,go(n_x,n_y,i)+a[x][y])
    dp[x][y][op]=ret
    return dp[x][y][op]
res=987654321
for i in range(M):
    res=min(res,go(0,i,3))
print(res)
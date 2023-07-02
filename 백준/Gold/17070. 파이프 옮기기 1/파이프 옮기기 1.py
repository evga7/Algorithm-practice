def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
#오,오아,아
dx=[0,1,1]
dy=[1,1,0]
import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
dp=[[[-1 for _ in range(N+1)] for _ in range(N+1)] for _ in range(3)]
def chk(idx,x,y):
    if idx==0:
        if a[x][y+1]:
            return False
        return True
    elif idx==1:
        if a[x][y+1] or a[x+1][y] or a[x+1][y+1]:
            return False
        return True
    else:
        if a[x+1][y]:
            return False
        return True
def go(op,x,y):
    if x==N-1 and y==N-1:
        return 1
    if dp[op][x][y]!=-1:
        return dp[op][x][y]
    ret=0
    for i in range(3):
        if op==0 and i==2:continue
        if op==2 and i==0:continue
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,N) and chk(i,x,y):
            ret+=go(i,n_x,n_y)
    dp[op][x][y]=ret
    return dp[op][x][y]
print(go(0,0,1))
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
b=[[0 for _ in range(M+1)] for _ in range(N+1)]
c=[[0 for _ in range(M+1)] for _ in range(N+1)]
H,W,sx,sy,ex,ey=map(int,input().split())
sx-=1
sy-=1
ex-=1
ey-=1
for i in range(1,N+1):
    for j in range(1,M+1):
        b[i][j]=a[i-1][j-1]+b[i-1][j]+b[i][j-1]-b[i-1][j-1]
q=deque()
q.append((0,sx,sy))
c[sx][sy]=1

def chk(x,y):
    SX,SY,EX,EY=x,y,x+H,y+W
    if not is_inside(x+H-1,y+W-1,N,M):
        return False
    if b[EX][EY]-b[EX][SY]-b[SX][EY]+b[SX][SY]:
        return False
    return True
while q:
    cost,x,y=q.popleft()
    if x==ex and y==ey:
        print(cost)
        exit(0)
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,M) and not c[n_x][n_y] and chk(n_x,n_y):
            c[n_x][n_y]=1
            q.append((cost+1,n_x,n_y))
print(-1)

import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
b=[[0 for _ in range(M+1)] for _ in range(N+1)]
K=int(input())
for i in range(1,N+1):
    for j in range(1,M+1):
        b[i][j]=b[i-1][j]+b[i][j-1]-b[i-1][j-1]+a[i-1][j-1]
for i in range(K):
    sx,sy,ex,ey=map(int,input().split())
    print(b[ex][ey]-b[ex][sy-1]-b[sx-1][ey]+b[sx-1][sy-1])
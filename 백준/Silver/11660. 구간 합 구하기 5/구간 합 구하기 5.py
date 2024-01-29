import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
# map(int,input().split())
INF = sys.maxsize
N,M=map(int,input().split())
def p(x1,y1,x2,y2):
    print(b[x2][y2]-b[x2][y1-1]-b[x1-1][y2]+b[x1-1][y1-1])
a=[list(map(int,input().split())) for _ in range(N)]
b=[[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        b[i][j]=a[i-1][j-1]+b[i-1][j]+b[i][j-1]-b[i-1][j-1]
for i in range(M):
    x1,y1,x2,y2=map(int,input().split())
    p(x1,y1,x2,y2)
import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
M=int(input())
g=[[987654321 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    g[a][b]=min(g[a][b],c)
for i in range(1,N+1):
    g[i][i]=0
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if g[i][k]+g[k][j]<g[i][j]:
                g[i][j]=g[i][k]+g[k][j]
for i in range(1,N+1):
    for j in range(1,N+1):
        if g[i][j]>=987654321:
            g[i][j]=0
        print(g[i][j],end=' ')
    print('')
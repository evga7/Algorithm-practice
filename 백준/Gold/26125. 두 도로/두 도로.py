import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
a=[]
N,M,S,T=map(int,input().split())
g=[[] for _ in range(N+1)]
dist=[[987654321 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    dist[a][b]=min(dist[a][b],c)
Q=int(input())
for i in range(1,N+1):
    dist[i][i]=0
def go():
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if dist[i][k]+dist[k][j]<dist[i][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
go()
for i in range(Q):
    x,y,c,x2,y2,c2=map(int,input().split())
    o=dist[x][y]
    o2=dist[x2][y2]
    dist[x][y]=min(dist[x][y],c)
    dist[x2][y2]=min(dist[x2][y2],c2)
    l=dist[S][T]
    l2=dist[S][x]+dist[x][y]+dist[y][T]
    l3 = dist[S][x2] + dist[x2][y2] + dist[y2][T]
    l4=dist[S][x]+dist[x][y]+dist[y][x2]+dist[x2][y2]+dist[y2][T]
    l5 = dist[S][x2] + dist[x2][y2] + dist[y2][x] + dist[x][y] + dist[y][T]
    res=min(l,l2,l3,l4,l5)
    if res>=987654321:
        print(-1)
    else:
        print(res)
    dist[x][y] = o
    dist[x2][y2] = o2
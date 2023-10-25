

import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
g=[[] for _ in range(N+1)]
dist=[[987654321 for _ in range(N+1)] for _ in range(N+1)]
def go():
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if i==j:continue
                if dist[i][k]+dist[k][j]<dist[i][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
    
        
for i in range(M):
    a,b,c=map(int,input().split())
    dist[a][b]=c
K=int(input())
a=list(map(int,input().split()))
go()
m=987654321
dist2=[0 for _ in range(N+1)]
for i in range(1,N+1):
    b=0
    for cur in a:
        if i==cur:continue
        b=max(b,dist[cur][i]+dist[i][cur])
    dist2[i]=b
m=min(dist2[1:])
for i in range(1,N+1):
    if m==dist2[i]:
        print(i,end=' ')
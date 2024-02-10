import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N,M=map(int,input().split())
g=[[987654321 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    g[a][b]=1
    g[b][a]=1
for i in range(1,N+1):
    g[i][i]=0
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if g[i][k]+g[k][j]<g[i][j]:
                g[i][j]=g[i][k]+g[k][j]
m=987654321
for i in range(1,N+1):
    s=sum(g[i][1:])
    if m>s:
        res=i
        m=s
print(res)
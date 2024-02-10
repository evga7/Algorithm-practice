import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N,M=map(int,input().split())
g=[[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    g[a][b]=1
    g[b][a]=1
res=0
for i in range(1,N+1):
    for j in range(i+1,N+1):
        for k in range(j+1,N+1):
            if g[i][j] or g[i][k] or g[j][k]:continue
            res+=1
print(res)
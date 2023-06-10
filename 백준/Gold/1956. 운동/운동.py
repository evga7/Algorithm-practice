import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
g=[[987654321 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    g[a][b]=c


for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if g[i][k]+g[k][j]< g[i][j]:
                g[i][j]=g[i][k]+g[k][j]
res=987654321
for i in range(1,N+1):
    res=min(res,g[i][i])
if res==987654321:
    res=-1
print(res)
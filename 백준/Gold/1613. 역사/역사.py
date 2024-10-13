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
p=[[987654321 for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    p[a][b]=1

K=int(input())
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if p[i][k]+p[k][j]<p[i][j]:
                p[i][j]=p[i][k] + p[k][j]
for i in range(K):
    a,b=map(int,input().split())
    if p[a][b]<p[b][a]:
        print(-1)
    elif p[a][b]>p[b][a]:
        print(1)
    else:
        print(0)
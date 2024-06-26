import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
g=[[0 for _ in range(N+1)] for _ in range(N+1)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if a[i][k] and a[k][j]:
                a[i][j]=1
for i in range(N):
    print(*a[i])
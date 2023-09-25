import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
a=[list(map(int,input())) for _ in range(N)]
res=0
def rev(x,y):
    for i in range(x+1):
        for j in range(y+1):
            a[i][j]=1-a[i][j]
for i in range(N-1,-1,-1):
    for j in range(M-1,-1,-1):
        if a[i][j]:
            res+=1
            rev(i,j)
print(res)
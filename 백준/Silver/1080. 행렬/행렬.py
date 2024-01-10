import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
a=[list(map(int,input())) for _ in range(N)]
b=[list(map(int,input())) for _ in range(N)]
res=0
def d():
    for i in range(N):
        for j in range(M):
            if a[i][j]!=b[i][j]:
                return False
    return True
def f(x,y):
    for i in range(x,min(x+3,N)):
        for j in range(y,min(y+3,M)):
            a[i][j]=1-a[i][j]
if d():
    print(res)
    exit(0)
for i in range(N-2):
    for j in range(M-2):
        if a[i][j]!=b[i][j]:
            f(i,j)
            res+=1
            if d():
                print(res)
                exit(0)
print(-1)
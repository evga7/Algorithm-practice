import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(map(int,input())) for _ in range(N)]
b=[list(map(int,input())) for _ in range(N)]
def go(x,y):
    for i in range(x,min(x+3,N)):
        for j in range(y,min(y+3,M)):
            a[i][j]=1-a[i][j]
res=0
if N>=3 and M>=3:
    for i in range(N-2):
        for j in range(M-2):
            if a[i][j]!=b[i][j]:
                go(i,j)
                res+=1
for i in range(N):
    for j in range(M):
        if a[i][j]!=b[i][j]:
            print(-1)
            exit(0)
print(res)
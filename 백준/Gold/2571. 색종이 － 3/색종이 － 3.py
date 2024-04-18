import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
N=int(input())
a=[[-10001 for _ in range(101)] for _ in range(101)]
b=[[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    x,y=map(int,input().split())
    for i in range(x,min(x+10,101)):
        for j in range(y,min(y+10,101)):
            a[i][j]=1
for i in range(1,101):
    for j in range(1,101):
        b[i][j]=b[i][j-1]+b[i-1][j]-b[i-1][j-1]+a[i][j]
res=0
for i in range(1,101):
    for j in range(1,101):
        for k in range(i+1,101):
            for l in range(j+1,101):
                s=b[k][l]-b[k][j-1]-b[i-1][l]+b[i-1][j-1]
                res=max(res,s)
print(res)
from collections import *
#sys.setrecursionlimit(100000)
dx = [1, -1, 0, 0]  # 아 위 오 왼
dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
N,M=map(int,input().split())
p=[i for i in range(N+1)]
def find(x):
    if x==p[x]:
        return x
    p[x]=find(p[x])
    return p[x]
def uni(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        if x<y:
            p[y]=x
        else:
            p[x]=y
        return True
    return False
a=list(input().split())
m=defaultdict(int)
for i,cur in enumerate(a):
    m[i+1]=cur
b=[list(map(int,input().split())) for _ in range(M)]
b.sort(key=lambda x:x[2])
res=0
for cur in b:
    x,y,cost=cur[0],cur[1],cur[2]
    a,b=m[x],m[y]
    if a!=b and uni(x,y):
        res+=cost
num=find(1)
for i in range(2,N+1):
    if num!=find(i):
        print(-1)
        exit(0)
print(res)
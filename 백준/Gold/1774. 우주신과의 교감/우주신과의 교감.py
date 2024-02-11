import sys
import math
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
b=[]
def dist(x,y,x2,y2):
    return math.sqrt(pow( abs(x - x2), 2 ) + pow( abs(y - y2), 2 ) )
for i in range(N):
    x,y=a[i][0],a[i][1]
    for j in range(i+1,N):
        x2,y2=a[j][0],a[j][1]
        b.append((dist(x,y,x2,y2),i,j))
b.sort()
p=[i for i in range(N+1)]
res=0
def find(x):
    if x==p[x]:
        return p[x]
    p[x]=find(p[x])
    return p[x]
def uni(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        if x>y:
            p[y]=x
        else:
            p[x]=y
        return True
    return False
for i in range(M):
    q,w=map(int,input().split())
    q-=1
    w-=1
    uni(q,w)
for cur in b:
    cost,X,Y=cur[0],cur[1],cur[2]
    if uni(X,Y):
        res+=cost
print("%.2f"%res)
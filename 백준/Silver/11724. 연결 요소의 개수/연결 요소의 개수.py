import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
p=[i for i in range(N+1)]
def find(x):
    if p[x]==x:
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
for i in range(M):
    a,b=map(int,input().split())
    uni(a,b)
res=1
x=find(1)
for i in range(2,N+1):
    if uni(x,i):
        res+=1
print(res)
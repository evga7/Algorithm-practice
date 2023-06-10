import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
M=int(input())
a=[list(map(int,input().split())) for _ in range(M)]
a.sort(key=lambda x:x[2])
res=0
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
        p[y]=x
        return True
    return False
for x in a:
    a,b,cost=x[0],x[1],x[2]
    if uni(a,b):
        res+=cost
print(res)
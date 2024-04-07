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
N=int(input())
M=int(input())
p=[i for i in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    uni(a,b)
c=find(1)
res=N-1
for i in range(1,N+1):
    if c!=find(i):
        res-=1
print(res)
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
N,M=map(int,input().split())
p=[i for i in range(N+1)]
a=[list(map(int,input().split())) for _ in range(M)]
a.sort(key=lambda x:x[2])
res=0
st=set()
c=0
for cur in a:
    x,y,cost=cur[0],cur[1],cur[2]
    if uni(x,y):
        res+=cost
        c=cost
print(res-c)
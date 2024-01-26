import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
#map(int,input().split())
INF=sys.maxsize
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
res=0
for i in range(M):
    a,b=map(int,input().split())
    if not uni(a,b):
        res+=1

st=set()
for i in range(1,N+1):
    st.add(find(i))
print(res+len(st)-1)
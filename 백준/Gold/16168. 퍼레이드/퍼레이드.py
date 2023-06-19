import sys
def input(): return sys.stdin.readline().rstrip()
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
        p[y]=x
        return True
    return False
c=[0 for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    uni(a,b)
    c[a]+=1
    c[b]+=1

r=find(1)
for i in range(2,N+1):
    if r!=find(i):
        print("NO")
        exit(0)
cnt=0
for i in range(1,N+1):
    if c[i]&1:
        cnt+=1
if not cnt or cnt==2:
    print("YES")
else:
    print("NO")
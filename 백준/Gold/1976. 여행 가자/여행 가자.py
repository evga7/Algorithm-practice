from collections import *
import sys
def input():return sys.stdin.readline().rstrip()

N=int(input())
M=int(input())
g=[[] for _ in range(N+1)]
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
        p[y]=x
        return True
    return False
for i in range(N):
    a=list(map(int,input().split()))
    for j in range(N):
        if a[j]:
            g[i+1].append(j+1)
a=list(map(int,input().split()))
d=[]
q=deque()
q.append(a[0])
while q:
    cur=q.popleft()
    d.append(cur)
    for nxt in g[cur]:
        if uni(cur,nxt):
            q.append(nxt)
t=p[a[0]]
f=1
for cur in a:
    if t!=p[cur]:
        f=0
        break
if f:
    print("YES")
else:
    print("NO")
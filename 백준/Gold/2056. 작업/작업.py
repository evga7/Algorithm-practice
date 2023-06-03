from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
g=[[] for _ in range(N+1)]
t=[0 for _ in range(N+1)]
p=[0 for _ in range(N+1)]
dist=[0 for _ in range(N+1)]
for i in range(N):
    a=list(map(int,input().split()))
    t[i+1]=a[0]
    p[i+1]=a[1]
    for j in range(2,len(a)):
        g[a[j]].append(i+1)

q=deque()
res=0
for i in range(1,N+1):
    if not p[i]:
        q.append((i,t[i]))
        dist[i]=t[i]
while q:
    x,cost=q.popleft()
    res=max(res,cost)
    for nxt in g[x]:
        p[nxt]-=1
        if dist[nxt]<t[nxt]+dist[x]:
            dist[nxt]=t[nxt]+dist[x]
        if not p[nxt]:
            q.append((nxt,cost+t[nxt]))
print(max(dist))
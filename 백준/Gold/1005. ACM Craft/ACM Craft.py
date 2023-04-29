from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
T=int(input())
def go():
    q=deque()
    for i in range(1,N+1):
        if not de[i]:
            q.append(i)
            dist[i]=a[i]
    while q:
        x=q.popleft()
        for nxt in g[x]:
            de[nxt]-=1
            if not de[nxt]:
                 q.append(nxt)
            dist[nxt]=max(dist[nxt],dist[x]+a[nxt])
    return dist[W]
while T:
    T-=1
    N,K=map(int,input().split())
    de = [0 for _ in range(N + 1)]
    g=[[] for _ in range(N+1)]
    a=[0]
    b=list(map(int,input().split()))
    for cur in b:
        a.append(cur)
    dist=[0 for _ in range(N+1)]
    for i in range(K):
        c,d=map(int,input().split())
        de[d]+=1
        g[c].append(d)
    W=int(input())
    print(go())

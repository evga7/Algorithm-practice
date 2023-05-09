from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
T=int(input())

def go(n1,n2):
    while depth[n1]>depth[n2]:
        n1=p[n1]
    while depth[n1]<depth[n2]:
        n2=p[n2]
    while n1!=n2:
        if p[n1]:
            n1=p[n1]
        if g[n2]:
            n2=p[n2]
    return n1
def go2(n1):
    ret=0
    if g[n1]:
        ret+=go2(g[n1])+1
    return ret
while T:
    T-=1
    N=int(input())
    p=[0 for _ in range(N+1)]
    g=[[] for _ in range(N+1)]
    depth=[0 for _ in range(N+1)]
    for i in range(N-1):
        a,b=map(int,input().split())
        p[b]=a
        g[a].append(b)
        g[b].append(a)
    c,d=map(int,input().split())
    top=0
    for i in range(1,N+1):
        if not p[i]:
            top=i
            break
    q=deque()
    q.append(top)
    v=[0 for _ in range(N+1)]
    v[top]=1
    while q:
        cur=q.popleft()
        for nxt in g[cur]:
            if not v[nxt]:
                v[nxt]=1
                depth[nxt]=depth[cur]+1
                q.append(nxt)
    print(go(c,d))
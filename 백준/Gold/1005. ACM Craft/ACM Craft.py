from collections import *
import bisect
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
T=int(input())
def go():
    q=deque()
    for i in range(1,N+1):
        if not p[i]:
            q.append(i)
            dist[i]=a[i-1]
    while q:
        cur=q.popleft()
        for nxt in g[cur]:
            p[nxt]-=1
            if not p[nxt]:
                q.append(nxt)
            dist[nxt]=max(dist[nxt],dist[cur]+a[nxt-1])

while T:
    T-=1
    g=defaultdict(list)
    N,M=map(int,input().split())
    p=[0 for _ in range(N+1)]
    a=list(map(int,input().split()))
    for i in range(M):
        q,w=map(int,input().split())
        g[q].append(w)
        p[w]+=1
    W=int(input())
    dist=[0 for _ in range(N+1)]
    go()
    print(dist[W])
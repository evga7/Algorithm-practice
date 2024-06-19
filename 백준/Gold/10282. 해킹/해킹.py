from collections import *
#sys.setrecursionlimit(100000)
dx = [1, -1, 0, 0]  # 아 위 오 왼
dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

import math
import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
T=int(input())
def go(c):
    q=deque()
    q.append(((0,c)))
    r1,r2=0,0
    dist=[987654321 for _ in range(10001)]
    dist[c]=0
    st=set()
    while q:
        cost,cur=q.popleft()
        if dist[cur]<cost:continue
        st.add(cur)
        for cur in g[cur]:
            nxt,n_cost=cur[0],cur[1]+cost
            if dist[nxt]>n_cost:
                dist[nxt]=n_cost
                q.append((n_cost,nxt))
    for i in range(1,n+1):
        if dist[i]!=987654321:
            r2=max(r2,dist[i])
    return (len(st),r2)
        
while T:
    T-=1
    n,d,c=map(int,input().split())
    g=[[] for _ in range(n+1)]
    for i in range(d):
        a, b, s = map(int, input().split())
        g[b].append((a,s))
    res1,res2=go(c)
    print(res1,res2)
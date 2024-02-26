import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
N=int(input())
g=[[] for _ in range(N+1)]
st=set()
visited=[0 for _ in range(N+1)]
v=[]
for i in range(N):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
def go(start,x,cnt):
    if x==start and cnt>3:
        st.add(start)
        for cur in v:
            st.add(cur)
        return 
    for nxt in g[x]:
        if visited[nxt]:continue
        visited[nxt]=1
        v.append(nxt)
        go(start,nxt,cnt+1)
        visited[nxt]=0
        v.pop()
for i in range(1,N+1):
    if i in st:continue
    go(i,i,1)
def go2(start):
    q=[]
    dist=[987654321 for _ in range(N+1)]
    q.append((0,start))
    dist[start]=0
    while q:
        cost,x=heapq.heappop(q)
        if x in st:
            return cost
        for nxt in g[x]:
            if dist[nxt]>cost+1:
                dist[nxt]=cost+1
                heapq.heappush(q,(cost+1,nxt))
    
for i in range(1,N+1):
    if i in st:
        print(0,end=' ')
    else:
        print(go2(i),end=' ')
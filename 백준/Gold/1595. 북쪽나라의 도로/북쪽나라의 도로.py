from collections import *
#sys.setrecursionlimit(100000)
#dx = [1, -1, 0, 0]  # 아 위 오 왼
#dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

import math
import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
g=[[] for _ in range(10001)]
while True:
    try:
        a,b,c=map(int,input().split())
        g[a].append((b,c))
        g[b].append((a,c))
    except:
        break
def go(start):
    q=deque()
    q.append((0,start))
    dist = [987654321 for _ in range(10001)]
    dist[start]=0
    while q:
        cost,cur=q.popleft()
        for nxt,c in g[cur]:
            n_cost=c+cost
            if dist[nxt]>n_cost:
                dist[nxt]=n_cost
                q.append((n_cost,nxt))
    m=0
    num=1
    for i in range(1,10001):
        if dist[i]!=987654321:
            if m<dist[i]:
                m=dist[i]
                num=i
    return (num,m)
start,m=go(1)

s,res=go(start)
print(res)
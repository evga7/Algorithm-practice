from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
M=int(input())
g=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
q=deque()
q.append(1)
v=[0 for _ in range(N+1)]
v[1]=1
res=0
while q:
    cur=q.popleft()
    for nxt in g[cur]:
        if not v[nxt]:
            v[nxt]=1
            res+=1
            q.append(nxt)
print(res)
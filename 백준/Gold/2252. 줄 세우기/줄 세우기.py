from collections import *
#sys.setrecursionlimit(100000)
N,M=map(int,input().split())
p=[0 for _ in range(N+1)]
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    p[b]+=1
    g[a].append(b)
q=deque()
for i in range(1,N+1):
    if not p[i]:
        q.append(i)
while q:
    cur=q.popleft()
    print(cur,end=' ')
    for nxt in g[cur]:
        p[nxt]-=1
        if not p[nxt]:
            q.append(nxt)
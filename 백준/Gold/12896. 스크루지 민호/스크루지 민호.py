import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
g=[[] for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
q=[]
dist=[987654321 for _ in range(N+1)]
q.append((1,0))
dist[1]=0
while q:
    x,cost=q.pop()
    for nxt in g[x]:
        if dist[nxt]>cost+1:
            dist[nxt]=cost+1
            q.append((nxt,cost+1))
res=0
m=0
idx=1
for i in range(1,N+1):
    if dist[i]>m:
        m=dist[i]
        idx=i
dist=[987654321 for _ in range(N+1)]
q.append((idx,0))
dist[idx]=0
while q:
    x,cost=q.pop()
    for nxt in g[x]:
        if dist[nxt]>cost+1:
            dist[nxt]=cost+1
            q.append((nxt,cost+1))
res=max(dist[1:])+1
print(res//2)
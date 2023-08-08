import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
import sys
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
st=[0 for _ in range(100001)]
visited=set()
N,M=map(int,input().split())
q=[]
q.append((0,N))
while q:
    cost,x=heapq.heappop(q)
    if x==M:
        print(cost)
        break
    for nxt in (x*2,x-1,x+1):
        if 0<=nxt<=100000 and not nxt in visited:
            visited.add(nxt)
            heapq.heappush(q,(cost+1,nxt))
            st[nxt]=x
res_v=[]
while M!=N:
    res_v.append(M)
    M=st[M]
res_v.append(N)
res_v.reverse()
print(*res_v)
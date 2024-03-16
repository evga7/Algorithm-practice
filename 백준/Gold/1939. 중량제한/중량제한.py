from collections import *
# sys.setrecursionlimit(100000)
import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))
S,E=map(int,input().split())
def chk(mid):
    visited=[0 for _ in range(N+1)]
    q=deque()
    q.append(S)
    visited[S]=1
    while q:
        x=q.popleft()
        if x==E:
            return True
        for cur in g[x]:
            nxt,weight=cur[0],cur[1]
            if not visited[nxt] and weight>=mid:
                q.append(nxt)
                visited[nxt]=1
    return False
        
left=0
right=int(1e10)
while left<=right:
    mid=left+right>>1
    if chk(mid):
        left=mid+1
    else:
        right=mid-1
print(left-1)
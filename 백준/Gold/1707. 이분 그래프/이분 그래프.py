from collections import *
import sys
#sys.setrecursionlimit(10000)
def input():return sys.stdin.readline().rstrip()
T=int(input())

def go(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        cur = q.popleft()
        for nxt in g[cur]:
            if not visited[nxt]:
                visited[nxt]=visited[cur]*-1
                q.append(nxt)
            elif visited[nxt] == visited[cur]:
                return False

    return True
while T:
    T-=1
    N,M=map(int,input().split())
    g=[[] for _ in range(N+1)]
    visited = [0 for _ in range(N + 1)]
    f=0
    for i in range(M):
        a,b=map(int,input().split())
        g[a].append(b)
        g[b].append(a)
    for i in range(1,N+1):
        if not visited[i]:
            if not go(i):
                f=1
                break
        if f:
            break
    if not f:
        print("YES")
    else:
        print("NO")
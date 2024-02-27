import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N = int(input())
g = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
root = 1
res = 0
for i in range(N-1):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))

def go(cur, cnt):
    if visited[cur]: return
    visited[cur] = 1
    global res, root
    if res < cnt:
        res = cnt
        root = cur
    for x in g[cur]:
        nxt,cost=x[0],x[1]
        if visited[nxt]: continue
        go(nxt, cnt + cost)
go(1, 0)
visited = [0 for _ in range(N + 1)]
go(root, 0)
print(res)
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N = int(input())
g = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
root = 1
res = 0
for i in range(N):
    a = list(map(int, input().split()))
    idx=a[0]
    for j in range(1, len(a) - 1, 2):
        nxt = a[j]
        if nxt == -1:
            break
        cost = a[j + 1]
        g[idx].append((nxt, cost))
        g[nxt].append((idx, cost))
def go(cur, cnt):
    if visited[cur]: return
    visited[cur] = 1
    global res, root
    if res < cnt:
        res = cnt
        root = cur
    for x in g[cur]:
        nxt, cost = x[0], x[1]
        if visited[nxt]: continue
        go(nxt, cnt + cost)
go(1, 0)
visited = [0 for _ in range(N + 1)]
go(root, 0)
print(res)


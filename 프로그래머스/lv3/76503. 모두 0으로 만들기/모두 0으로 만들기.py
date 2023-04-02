import sys
sys.setrecursionlimit(300001)
v=[0 for _ in range(300001)]
g=[[] for _ in range(300001)]
res=0
def go(cur,a):
    v[cur]=1
    for nxt in g[cur]:
        if v[nxt]:continue
        a[cur]+=go(nxt,a)
    global res
    res+=abs(a[cur])
    return a[cur]
def solution(a, edges):
    if sum(a):
        return -1
    for cur in edges:
        g[cur[0]].append(cur[1])
        g[cur[1]].append(cur[0])
    go(0,a)
    global res
    return res
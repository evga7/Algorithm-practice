from collections import *
def solution(n, roads, sources, destination):
    answer = []
    d=[987654321 for _ in range(n+1)]
    g=[[] for _ in range(n+1)]
    for cur in roads:
        a,b=cur[0],cur[1]
        g[a].append(b)
        g[b].append(a)
    q=deque()
    q.append((destination,0))
    d[destination]=0
    while q:
        x,c=q.popleft()
        for nxt in g[x]:
            if d[nxt]>c+1:
                d[nxt]=c+1
                q.append((nxt,c+1))
    for cur in sources:
        a=-1
        if d[cur]!=987654321:
            a=d[cur]
        answer.append(a)
    return answer
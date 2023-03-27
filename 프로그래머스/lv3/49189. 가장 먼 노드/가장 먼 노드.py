from collections import *
def solution(n, edge):
    g=[[] for _ in range(n+1)]
    answer = 0
    for cur in edge:
        x,y=cur[0],cur[1]
        g[x].append(y)
        g[y].append(x)
    q=deque()
    q.append((1,0))
    d=[987564321 for _ in range(n+1)]
    d[1]=0
    m=0
    while q:
        x,c=q.popleft()
        m=max(m,c)
        for nxt in g[x]:
            if d[nxt]>c+1:
                d[nxt]=c+1
                q.append((nxt,c+1))
    for i in range(1,n+1):
        if d[i]==m:
            answer+=1
    return answer
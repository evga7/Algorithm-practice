N,M=map(int,input().split())
g=[]
for i in range(M):
    a,b,c=map(int,input().split())
    g.append((a,b,c))
dist=[987654321 for _ in range(N+1)]
dist[1]=0
for r in range(N):
    for i in range(M):
        cur,nxt,cost=g[i][0],g[i][1],g[i][2]
        n_cost=dist[cur]+cost
        if dist[cur]!=987654321 and dist[nxt]>n_cost:
            dist[nxt]=n_cost
            if r==N-1:
                print(-1)
                exit(0)
for i in range(2,N+1):
    if dist[i]==987654321:
        dist[i]=-1
    print(dist[i])
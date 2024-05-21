from collections import *
dx=[-1,1,0,0]
dy=[0,0,1,-1]
def solution(maps):
    answer = 987654321
    n,m=len(maps),len(maps[0])
    dist=[[987654321 for _ in range(m)] for _ in range(n)]
    q=deque()
    q.append((0,0,0))
    while q:
        cost,x,y=q.popleft()
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if 0<=n_x<n and 0<=n_y<m and maps[n_x][n_y] and dist[n_x][n_y]>cost+1:
                dist[n_x][n_y]=cost+1
                q.append((cost+1,n_x,n_y))
                
    if dist[n-1][m-1]==987654321:
        dist[n-1][m-1]=-2
    
    return dist[n-1][m-1]+1
import heapq
import sys
def input():return sys.stdin.readline().rstrip()
dx=[0,0,1,-1,-1,1,1,-1]
dy=[1,-1,0,0,1,1,-1,-1]
idx=1
while 1:
    N=int(input())
    if not N:
        break
    arr=[list(map(int,input().split())) for _ in range(N)]
    q=[]
    q.append((arr[0][0],0,0))
    dist = [[987654321 for _ in range(126)] for _ in range(126)]
    while q:
        cost,x,y=heapq.heappop(q)
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if 0<=n_x<N and 0<=n_y<N:
                nc=cost + arr[n_x][n_y]
                if dist[n_x][n_y] > nc:
                    dist[n_x][n_y]=nc
                    q.append((nc,n_x,n_y))
    print("Problem %d: %d"%(idx,dist[N-1][N-1]))
    idx+=1
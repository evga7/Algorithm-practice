dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M

import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
a=[list(input()) for _ in range(N)]
sx,sy=0,0
visited=[[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        if a[i][j]=='S':
            sx=i
            sy=j
q=[]
q.append((0,0,sx,sy))
def chk(x,y):
    cnt=0
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,M) and a[n_x][n_y]=='g':
            return 1
    return 0
visited[sx][sy]=1
while q:
    cost1,cost2,x,y=heapq.heappop(q)
    if a[x][y]=='F':
        print(cost1,cost2)
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,M) and not visited[n_x][n_y]:
            n_cost1=cost1
            n_cost2 = cost2
            if a[n_x][n_y]=='g':
                n_cost1+=1
            else:
                if a[n_x][n_y]!='F':
                    n_cost2+=chk(n_x,n_y)
            visited[n_x][n_y]=1
            heapq.heappush(q,(n_cost1,n_cost2,n_x,n_y))

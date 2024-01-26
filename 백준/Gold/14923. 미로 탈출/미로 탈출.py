dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
#map(int,input().split())
INF=sys.maxsize
N,M=map(int,input().split())
sx,sy=map(int,input().split())
ex,ey=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
dist=[[[987654321 for _ in range(M+1)] for _ in range(N+1)] for _ in range(2)]
q=[]
q.append((0,0,sx-1,sy-1))
while q:
    cost,block,x,y=heapq.heappop(q)
    if x==ex-1 and y==ey-1:
        print(cost)
        exit(0)
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,M):
            if a[n_x][n_y]:
                if not block:
                    if dist[1][n_x][n_y]>cost+1:
                        dist[1][n_x][n_y]=cost+1
                        heapq.heappush(q,(cost+1,1,n_x,n_y))
            else:
                if dist[block][n_x][n_y]>cost+1:
                    dist[block][n_x][n_y]=cost+1
                    heapq.heappush(q, (cost + 1, block, n_x, n_y))
                    
            
print(-1)
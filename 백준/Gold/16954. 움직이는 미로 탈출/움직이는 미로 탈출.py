dx=[-1,-1,-1,0,1,1,1,0,0]
dy=[-1,0,1,1,1,0,-1,-1,0]
# dx = [-1,1,0,0]  # 위 아 오 왼
# dy = [0,0,1,-1]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
import copy
from collections import *
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
a=[list(input()) for _ in range(8)]
q=deque()
visited=[[[0 for _ in range(9)] for _ in range(8)] for _ in range(8)]
q.append((7,0,0))
while q:
    x,y,n=q.popleft()
    if x==0 and y==7:
        print(1)
        exit(0)
    for i in range(9):
        n_x=x+dx[i]
        n_y=y+dy[i]
        n_n=min(n+1,8)
        if is_inside(n_x,n_y,8,8) and not visited[n_x][n_y][n_n]:
            if n_x-n>=0:
                if a[n_x - n][n_y] != '#':
                    if n_x-n_n>=0: 
                        if a[n_x-n_n][n_y]!='#':
                            visited[n_x][n_y][n_n]=1
                            q.append((n_x,n_y,min(n+1,8)))    
            else:            
                visited[n_x][n_y][n_n] = 1
                q.append((n_x, n_y, n_n))
                
        
            
print(0)
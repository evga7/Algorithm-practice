import bisect
import heapq
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1,-1]
dy = [1, -1, 0, 0]
ddx=[-1,-2,-2,-1,1,2,2,1]
ddy=[-2,-1,1,2,2,1,-1,-2]
K=int(input())
M,N=map(int,input().split())
visited=[[[0 for _ in range(M+1)] for _ in range(N+1)] for _ in range(K+1)]
arr=[list(map(int,input().split())) for _ in range(N)]
q=[]
q.append((0,0,0,K))
while q:
    cost,x,y,k=heapq.heappop(q)
    if x==N-1 and y==M-1:
        print(cost)
        exit(0)
    if k:
        for i in range(8):
            n_x = x + ddx[i]
            n_y = y + ddy[i]
            if is_inside(n_x, n_y, N, M) and not arr[n_x][n_y] and not visited[k-1][n_x][n_y]:
                visited[k-1][n_x][n_y] = 1
                heapq.heappush(q,(cost + 1, n_x, n_y,k-1))
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,M) and not arr[n_x][n_y] and not visited[k][n_x][n_y]:
            visited[k][n_x][n_y]=1
            heapq.heappush(q,(cost+1,n_x,n_y,k))
print(-1)

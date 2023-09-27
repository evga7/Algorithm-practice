dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M

import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
v=[]
x,y=0,0
for i in range(N):
    for j in range(N):
        if a[i][j]:
            if a[i][j]==9:
                x=i
                y=j
                a[i][j]=-1
            else:
                v.append((i,j,a[i][j]))
v.sort()
def dis(sx,sy,des_x,des_y,cost):
    q=[]
    q.append((0,sx,sy))
    dist=[[987654321 for _ in range(N)] for _ in range(N)]
    dist[sx][sy]=0
    while q:
        d,x,y=heapq.heappop(q)
        if x==des_x and des_y==y:
            return d
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,N) and a[n_x][n_y]<=cost and dist[n_x][n_y]>d+1:
                dist[n_x][n_y]=d+1
                heapq.heappush(q,(d+1,n_x,n_y))
    return -1
def chk(sx,sy,cost):
    dist=987654321
    idx=-1
    for i in range(len(v)):
        n_x,n_y,n_cost=v[i]
        if cost>n_cost:
            n_dist = dis(sx, sy, n_x, n_y, cost)
            if dist>n_dist and n_dist!=-1:
                dist=n_dist
                idx=i
    return (idx,dist)
            
        
def go(x,y):
    cost=2
    cnt=0
    res=0
    cnt2=0
    while cnt2<len(v):
        (idx,dist)=chk(x,y,cost)
        if idx==-1:
            break
        n_x,n_y,n_cost=v[idx]
        cnt+=1
        if cnt==cost:
            cost+=1
            cnt=0
        a[x][y]=0
        x,y=n_x,n_y
        a[x][y]=-1
        res+=dist
        del v[idx]
    print(res)
go(x,y)
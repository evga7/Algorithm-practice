from collections import *
dx=[0,0,1,-1]
dy=[1,-1,0,0]
vi=[[0 for _ in range(301)] for _ in range(301)]
idx=1
p=[i for i in range(90001)]
def find(x):
    if p[x]==x:
        return x
    p[x]=find(p[x])
    return p[x]
def uni(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        p[y]=x
        return True
    return False
def go(i,j,N,M,l,h):
    global idx
    q=deque()
    q.append((i,j))
    vi[i][j]=idx
    while q:
        x,y=q.popleft()
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if 0<=n_x<N and 0<=n_y<M and not vi[n_x][n_y] and abs(l[x][y]-l[n_x][n_y])<=h:
                vi[n_x][n_y]=idx
                q.append((n_x,n_y))
    idx+=1
def solution(land, height):
    answer = 0
    N=len(land)
    M=len(land[0])
    for i in range(N):
        for j in range(M):
            if not vi[i][j]:
                go(i,j,N,M,land,height)
    v=[]
    for i in range(N):
        for j in range(M):
            for k in range(4):
                n_x=i+dx[k]
                n_y=j+dy[k]
                if 0 <= n_x < N and 0 <= n_y < M and vi[i][j]!=vi[n_x][n_y]:
                    v.append((abs(land[i][j]-land[n_x][n_y]),vi[i][j],vi[n_x][n_y]))
    v.sort()
    for cur in v:
        if uni(cur[1],cur[2]):
            answer+=cur[0]
    return answer
import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
res=0
dx=[[0,1],[0,-1],[-1,0],[1,0]]
dy=[[-1,0],[-1,0],[0,1],[0,1]]
visited=[[0 for _ in range(M)] for _ in range(N)]
def go2(op,x,y,op2):
    n_x = x + dx[op][0]
    n_y = y + dy[op][0]
    n_x2 = x + dx[op][1]
    n_y2 = y + dy[op][1]
    visited[x][y]=op2
    visited[n_x][n_y],visited[n_x2][n_y2]=op2,op2
    return a[x][y]*2+a[n_x][n_y]+a[n_x2][n_y2]



def go(x,s):
    global res
    res=max(res,s)
    for i in range(x,N):
        for j in range(M):
            for k in range(4):
                n_x=i+dx[k][0]
                n_y=j+dy[k][0]
                n_x2 = i + dx[k][1]
                n_y2 = j + dy[k][1]
                if not visited[i][j]  and 0<=n_x<N and 0<=n_y<M and 0<=n_x2<N and 0<=n_y2<M and not visited[n_x][n_y] and not visited[n_x2][n_y2]:
                    ss=go2(k,i,j,1)
                    go(i,s+ss)
                    go2(k,i,j,0)
go(0,0)
print(res)
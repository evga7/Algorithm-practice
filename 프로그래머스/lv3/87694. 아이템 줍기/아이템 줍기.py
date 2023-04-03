from collections import *
dx=[0,0,1,-1,-1,1,1,-1]
dy=[1,-1,0,0,1,1,-1,-1]
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    itemY*=2
    itemX*=2
    characterY*=2
    characterX*=2
    a=[[0 for _ in range(104)] for _ in range(104)]
    b = [[0 for _ in range(104)] for _ in range(104)]
    v = [[0 for _ in range(104)] for _ in range(104)]
    for cur in rectangle:
        x1,y1,x2,y2=cur[0]*2,cur[1]*2,cur[2]*2,cur[3]*2
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                a[i][j]=1
    q=deque()
    q.append((0,0))
    v[0][0]=1
    while q:
        x,y=q.popleft()
        for i in range(8):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if 0<=n_x<=101 and 0<=n_y<=101 and not v[n_x][n_y]:
                v[n_x][n_y] = 1
                if a[n_x][n_y]:
                    b[n_x][n_y]=1
                    continue
                q.append((n_x,n_y))
    v = [[987654321 for _ in range(104)] for _ in range(104)]
    q.append((characterX,characterY,0))
    v[characterX][characterY]=0
    while q:
        x,y,c=q.popleft()
        if x==itemX and y==itemY:
            return c//2
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if 1<=n_x<=100 and 1<=n_y<=100 and v[n_x][n_y]>c+1 and b[n_x][n_y]:
                v[n_x][n_y]=c+1
                q.append((n_x,n_y,c+1))
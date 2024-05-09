dx=[-1,1,0,0]
dy=[0,0,-1,1]
def is_inside(x,y,n,m):
    return 0<=x<n and 0<=y<m
def go(sx,sy,d,cnt,n,m,b):
    x,y=sx,sy
    while cnt:
        cnt-=1
        n_x=x+dx[d]
        n_y=y+dy[d]
        if is_inside(n_x,n_y,n,m) and b[n_x][n_y]!='X':
            x,y=n_x,n_y
        else:
            return sx,sy
    return x,y
def solution(park, routes):
    M={'E':3,'N':0,'S':1,'W':2}
    x,y=0,0
    n,m=len(park),len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j]=='S':
                x,y=i,j
                break
    for cur in routes:
        op,num=cur.split()
        x,y=go(x,y,M[op],int(num),n,m,park)
    return [x,y]
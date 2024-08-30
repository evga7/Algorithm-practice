dx=[0,1,0,-1]
dy=[1,0,-1,0]
def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    dir=0
    num=1
    x,y=0,0
    while True:
        answer[x][y]=num
        if num==n*n:break
        while True:
            n_x=x+dx[dir]
            n_y=y+dy[dir]
            if 0<=n_x<n and 0<=n_y<n and not answer[n_x][n_y]:
                break
            dir+=1
            dir%=4
        x,y=n_x,n_y
        num+=1
    return answer
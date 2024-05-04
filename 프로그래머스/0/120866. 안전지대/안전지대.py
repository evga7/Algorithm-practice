def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
dx=[-1,-1,-1,0,1,1,1,0]
dy=[0,-1,1,1,1,0,-1,-1]
def chk(x,y,n,m,board):
    for i in range(8):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,n,m) and not board[n_x][n_y]:
            board[n_x][n_y]=-1
def solution(board):
    answer = 0
    n=len(board)
    m=len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j]==1:
                chk(i,j,n,m,board)
    for i in range(n):
        for j in range(m):
            if not board[i][j]:
                answer+=1
    return answer
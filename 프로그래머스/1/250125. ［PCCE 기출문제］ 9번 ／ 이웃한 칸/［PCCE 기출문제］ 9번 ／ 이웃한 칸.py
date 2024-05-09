dx = [0,1,0,-1]
dy = [1,0,-1,0]
def solution(board, h, w):
    answer = 0
    N,M=len(board),len(board[0])
    for i in range(4):
        n_x=h+dx[i]
        n_y=w+dy[i]
        if 0<=n_x<N and 0<=n_y<M and board[h][w]==board[n_x][n_y]:
            answer+=1
    return answer
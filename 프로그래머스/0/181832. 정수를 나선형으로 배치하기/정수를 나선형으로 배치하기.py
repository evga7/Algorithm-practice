dx=[0,1,0,-1]
dy=[1,0,-1,0]
def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    x,y=0,0
    cnt=1
    d=0
    while True:
        answer[x][y]=cnt
        cnt+=1
        if cnt>n*n:
            break
        n_x,n_y=x+dx[d],y+dy[d]
        while not (0<=n_x<n and 0<=n_y<n) or answer[n_x][n_y]:
            d=(d+1)%4
            n_x=x+dx[d]
            n_y=y+dy[d]
        x,y=n_x,n_y
    return answer
print(solution(4))
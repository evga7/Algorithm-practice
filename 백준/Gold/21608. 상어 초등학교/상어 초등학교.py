dx = [1, -1, 0, 0]  # 아 위 오 왼
dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
N=int(input())
g=[set() for _ in range(N*N+1)]
m=[[0 for _ in range(N+1)] for _ in range(N+1)]
score={0:0,1:1,2:10,3:100,4:1000}
def find_pos(num,x,y):
    c=0
    empty=0
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,N):
            nxt=m[n_x][n_y]
            if nxt:
                if nxt in g[num]:
                    c+=1
            else:
                empty+=1
    return (empty,c)
def go(num):
    x,y=0,0
    c_cnt=-1
    empty_cnt=-1
    for i in range(N):
        for j in range(N):
            if not m[i][j]:
                empty,c=find_pos(num,i,j)
                if c_cnt<=c:
                    if c_cnt<c:
                        c_cnt=c
                        empty_cnt=empty
                        x,y=i,j
                    else:
                        if empty_cnt<empty:
                            empty_cnt=empty
                            x,y=i,j
    return (x,y)
            
for i in range(N*N):
    num,*a=list(map(int,input().split()))
    for cur in a:
        g[num].add(cur)
    x,y=go(num)
    m[x][y]=num
res=0
for i in range(N):
    for j in range(N):
        num=m[i][j]
        c=0
        for k in range(4):
            n_x=i+dx[k]
            n_y=j+dy[k]
            if is_inside(n_x,n_y,N,N):
                nxt=m[n_x][n_y]
                if nxt in g[num]:
                    c+=1
        res+=score[c]
print(res)
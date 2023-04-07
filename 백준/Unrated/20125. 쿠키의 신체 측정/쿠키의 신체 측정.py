import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
arr=[list(input()) for _ in range(N)]
sx,sy=0,0
dx=[0,0,1]
dy=[-1,1,0]
for i in range(N):
    for j in range(N):
        if arr[i][j]=='*':
            sx,sy=i+1,j
            break
    if sx and sy:
        break
print(sx+1,sy+1)
res_v=[]
for i in range(3):
    n_x=sx+dx[i]
    n_y=sy+dy[i]
    cnt=0
    while 0<=n_x<N and 0<=n_y<N and arr[n_x][n_y]=='*':
        cnt+=1
        n_x+=dx[i]
        n_y+=dy[i]
    res_v.append(cnt)
ssx=res_v[-1]
for i in range(2):
    cnt=0
    n_x=sx+ssx+1
    n_y=sy+dy[i]
    while 0<=n_x<N and 0<=n_y<N and arr[n_x][n_y]=='*':
        cnt+=1
        n_x+=1
    res_v.append(cnt)
print(*res_v)
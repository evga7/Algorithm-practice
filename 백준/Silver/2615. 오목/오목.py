def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import sys
dx=[0,1,1,-1]
dy=[1,1,0,1]
def input(): return sys.stdin.readline().rstrip()
a=[list(map(int,input().split())) for _ in range(19)]
v=[[[0 for _ in range(8)] for _ in range(19)] for _ in range(19)]
def go(x,y):
    val=a[x][y]
    for i in range(4):
        cnt=0
        n_x=x-dx[i]
        n_y=y-dy[i]
        if is_inside(n_x,n_y,19,19) and a[n_x][n_y]==val:
            continue
        for j in range(6):
            n_x+=dx[i]
            n_y+=dy[i]
            if is_inside(n_x,n_y,19,19) and val==a[n_x][n_y]:
                cnt+=1
            else:
                if cnt==5:
                    return (x, y, val)
                cnt=0
        if cnt==5:
            return (x,y,val)
    return (-1,-1,-1)


for i in range(19):
    for j in range(19):
        if a[i][j]:
            res=go(i,j)
            if res[0]!=-1:
                print(res[2])
                print(res[0]+1,res[1]+1)
                exit(0)

print(0)
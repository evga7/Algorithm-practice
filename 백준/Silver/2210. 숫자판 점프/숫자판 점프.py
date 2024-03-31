import sys
dx = [0,1,0,-1]  # 오 아 왼 위
dy = [1,0,-1,0]
dd=[0,4,2,4,4,1]
import heapq
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
def input():
    return sys.stdin.readline().rstrip()
a=[list(map(int,input().split())) for _ in range(5)]
res=0
st=set()
def go(x,y,s,cnt):
    if cnt==6:
        st.add(s)
        return
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,5,5):
            go(n_x,n_y,s*10+a[n_x][n_y],cnt+1)
for i in range(5):
    for j in range(5):
        go(i,j,a[i][j],1)
print(len(st))
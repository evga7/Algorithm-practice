def is_inside(x,y,N,M):
    return 0<=x<=N and 0<=y<=M

dx=[0,1]
dy=[1,0]
import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
K=int(input())
st=set()
for i in range(K):
    xx,yy,x2,y2=map(int,input().split())
    st.add((xx,yy,x2,y2))
dp=[[-1 for _ in range(101)] for _ in range(101)]
def go(x,y):
    if x==N and y==M:
        return 1
    if dp[x][y]!=-1:
        return dp[x][y]
    ret=0
    for i in range(2):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,M) and not (x,y,n_x,n_y) in st and not (n_x,n_y,x,y) in st:
            ret+=go(n_x,n_y)
    dp[x][y]=ret
    return dp[x][y]
print(go(0,0))
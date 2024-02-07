import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N,M,H=map(int,input().split())
dist=[[[-1 for _ in range(N+1)] for _ in range(N+1)] for _ in range(1025)]
a=[list(map(int,input().split())) for _ in range(N)]
sx,sy=-1,-1
v=[]
visited=[0 for _ in range(11)]
res=0
for i in range(N):
    for j in range(N):
        if a[i][j]==1:
            sx,sy=i,j
        elif a[i][j]==2:
            v.append((i,j))
def dis(x,y,n_x,n_y):
    return abs(x-n_x)+abs(y-n_y)
def go(x,y,hp,cnt):
    if hp<0:return
    if hp-dis(x,y,sx,sy)>=0 and cnt:
        global res
        res=max(res,cnt)
    for i in range(len(v)):
        if visited[i]:continue
        n_x, n_y = v[i][0], v[i][1]
        d=dis(x, y, n_x, n_y)
        if hp-d>=0:
            visited[i]=1
            go(n_x,n_y,hp-d+H,cnt+1)
            visited[i]=0
go(sx,sy,M,0)
print(res)
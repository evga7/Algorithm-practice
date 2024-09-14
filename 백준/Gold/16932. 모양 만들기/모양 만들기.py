from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
#dx=[0,1,0,-1,-1,-1,1,1]
#dy=[1,0,-1,0,-1,1,1,-1]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
visited=[[0 for _ in range(M+1)] for _ in range(N+1)]
m=defaultdict(int)
m2=defaultdict(set)
idx=0
res=0
def go(sx,sy):
    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=1
    while q:
        x,y=q.popleft()
        m[idx]+=1
        m2[(x,y)]=idx
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M) and a[n_x][n_y] and not visited[n_x][n_y]:
                visited[n_x][n_y]=1
                q.append((n_x,n_y))
                
for i in range(N):
    for j in range(M):
        if a[i][j] and not visited[i][j]:
            go(i,j)
            idx+=1
def go2(x,y):
    stt=set()
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if (n_x,n_y) in m2:
            stt.add(m2[(n_x,n_y)])
    global res
    c=0
    for cur in stt:
        c+=m[cur]
    res=max(res,c+1)
for i in range(N):
    for j in range(M):
        if not a[i][j]:
            go2(i,j)
print(res)
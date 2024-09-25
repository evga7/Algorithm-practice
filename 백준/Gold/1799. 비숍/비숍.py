import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
#dx=[0,1,0,-1,-1,-1,1,1]
#dy=[1,0,-1,0,-1,1,1,-1]
#dx=[0,0,1,-1]
#dy=[1,-1,0,0]
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
c=[0 for _ in range(2*N)]
res=0
v=[[] for _ in range(2*N)]
for i in range(N):
    for j in range(N):
        if a[i][j]:
            v[i+j].append((i,j))
l=len(v)

def go(idx,cnt):
    global res
    if res>=cnt+(l-idx):
        return
    res=max(res,cnt)
    if idx==l:
        return
    for x,y in v[idx]:
        c2=x-y
        if c2<=0:
            c2=abs(c2)+N-1
        if not c[c2]:
            c[c2]=1
            go(idx+1,cnt+1)
            c[c2]=0
    go(idx+1,cnt)
go(0,0)
print(res)
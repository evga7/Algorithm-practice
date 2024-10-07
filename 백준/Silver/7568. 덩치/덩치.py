import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)+7
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
#dx=[0,1,0,-1,-1,-1,1,1]
#dy=[1,0,-1,0,-1,1,1,-1]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
cnt=0
r=[]
v=[]
for i in range(N):
    x,y=a[i]
    rank=1
    for j in range(N):
        xx,yy=a[j]
        if x<xx and y<yy:
            rank+=1
    r.append(rank)
print(*r)
    
    
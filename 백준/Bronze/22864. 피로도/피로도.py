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
t=0
A,B,C,D=map(int,input().split())
tt=0
res=0
while t<24:
    if tt+A<=D:
        tt+=A
        res+=B
    else:
        tt=max(tt-C,0)
    t+=1
print(res)
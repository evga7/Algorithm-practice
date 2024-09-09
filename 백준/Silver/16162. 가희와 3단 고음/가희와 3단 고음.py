import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
dx=[0,1,0,-1,-1,-1,1,1]
dy=[1,0,-1,0,-1,1,1,-1]
N,A,D=map(int,input().split())
a=list(map(int,input().split()))
res=0
for cur in a:
    if A==cur:
        A+=D
        res+=1
print(res)
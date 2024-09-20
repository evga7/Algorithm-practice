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
N=int(input())
M=int(input())
a=list(map(int,input().split()))
m=defaultdict(int)
res=0
for cur in a:
    if M-cur in m:
        res+=m[M-cur]
    m[cur]+=1
print(res)
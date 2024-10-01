import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)+7
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
#dx=[0,1,0,-1,-1,-1,1,1]
#dy=[1,0,-1,0,-1,1,1,-1]
#dx=[0,0,1,-1]
#dy=[1,-1,0,0]
dx=[1,1,-1,-1]
dy=[1,-1,-1,1]
N=int(input())
a=int(math.sqrt(N))
if a*a>=N:
    print(a)
else:
    print(a+1)
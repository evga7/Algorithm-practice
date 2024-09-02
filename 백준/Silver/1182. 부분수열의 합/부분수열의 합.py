import itertools
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
dx=[0,1,0,-1,-1,-1,1,1]
dy=[1,0,-1,0,-1,1,1,-1]
N,M=map(int,input().split())
a=list(map(int,input().split()))
res=0
def go(idx,s):
    if idx==N:
        if s==M:
            global res
            res+=1
        return
    go(idx+1,s)
    go(idx + 1, s+a[idx])
go(0,0)
if M==0:
    res-=1
print(res)
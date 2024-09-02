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
N=int(input())
a=[list(map(int,input())) for _ in range(N)]
def go(x,y,l):
    zero,one=1,1
    for i in range(x,x+l):
        for j in range(y,y+l):
            if a[i][j]==1:
                zero=0
            else:
                one=0
        if not one and not zero:
            break
    if not one and not zero:
        print('(',end='')
        half=l//2
        go(x,y,half)
        go(x,y+half,half)
        go(x+half,y,half)
        go(x+half,y+half,half)
        print(')', end='')
    else:
        if one:
            print(1,end='')
        else:
            print(0,end='')
go(0,0,N)
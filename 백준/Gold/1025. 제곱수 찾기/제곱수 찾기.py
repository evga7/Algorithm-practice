import math
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
a=[list(input()) for _ in range(N)]
res=-1
st=set()
def go(x,y,s,c1,c2,op):
    global res
    if s:
        ss = s[::-1]
        num = int(s)
        num2 = int(ss)
        mt = math.sqrt(num)
        mt2 = math.sqrt(num2)
        if int(mt) == mt:
            res = max(res, num)
        if int(mt2) == mt2:
            res = max(res, num2)
    if not is_inside(x,y,N,M):
        return
    if not op:
        go(x+c1,y+c2,s+a[x][y],c1,c2,op)
    else:
        go(x + c1, y - c2, s + a[x][y], c1, c2,op)
for i in range(N):
    for j in range(M):
        for k in range(10):
            for l in range(10):
                if k==0 and l==0:continue
                go(i,j,'',k,l,1)
                go(i, j, '', k, l, 0)
print(res)
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
N=int(input())
res=987654321
def chk(num):
    if num==1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if not num%i:
            return False
    return True
def go(cnt,s):
    if cnt==8:
        return
    int_s =0
    if s:
        int_s=int(s)
    global res
    if res<int_s:
        return
    if int_s>=N and chk(int_s):
        res=min(res,int(s))
        return
    for i in range(9,-1,-1):
        go(cnt+1,str(i)+s+str(i))
NN=str(N)
go(0,'')
for i in range(10):
    go(1,str(i))
print(res)
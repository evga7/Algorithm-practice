import sys
from collections import *
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
a=list(map(int,input().split()))
M=int(input())
s=0
cnt=0
m=defaultdict(int)
def chk(c,d):
    while d:
        temp=c%d
        c=d
        d=temp
    return c
for cur in a:
    q=-1
    if not cur in m:
        q=chk(cur,M)
    if q==1:
        s += cur
        cnt += 1
print(s/cnt)
    
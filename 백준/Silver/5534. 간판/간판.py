import heapq
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
#dx=[0,1,0,-1,-1,-1,1,1]
#dy=[1,0,-1,0,-1,1,1,-1]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
N=int(input())
s=input()
res=0
st=set(s)
for i in range(N):
    s2=input()
    idx=0
    cnt=0
    m=defaultdict(set)
    f=0
    for i,cur in enumerate(s2):
        if cur==s[0]:
            for j in range(1,100):
                if f:
                    break
                idx = 1
                for k in range(i+j,len(s2),j):
                    if s[idx]==s2[k]:
                        idx+=1
                    else:
                        break
                    if idx==len(s):
                        f=1
                        break
    if f:
        res+=1

print(res)


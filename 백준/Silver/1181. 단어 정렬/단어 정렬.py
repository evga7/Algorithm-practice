from functools import cmp_to_key
from typing import List

dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
a=[input() for _ in range(N)]
st=set(a)
b=list(st)
def cmp(s1,s2):
    if len(s1)<len(s2):
        return -1
    elif len(s1)>len(s2):
        return 1
    else:
        if s1<s2:
            return -1
        else:
            return 1
b.sort(key=cmp_to_key(cmp))
for cur in b:
    print(cur)
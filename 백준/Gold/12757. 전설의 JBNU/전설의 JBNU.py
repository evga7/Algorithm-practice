import bisect
import math
import re

import itertools
import collections
#sys.setrecursionlimit(10 ** 6)
from collections import *
from functools import cmp_to_key
from typing import List

dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M

import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
#map(int,input().split())
INF=sys.maxsize
N,M,K=map(int,input().split())
m=defaultdict(int)
b=[]
def find_num(num):
    if num in m:
        return num
    idx=bisect.bisect(b,num)
    l=len(b)
    if l>idx and idx>0:
        s1=abs(num-b[idx-1])
        s2=abs(num-b[idx])
        if s1==s2:
            return -2
        elif s1<=s2 and s1<=K :
            return b[idx-1]
        elif s1>=s2 and s2<=K:
            return b[idx]
        else:
            return -1
    elif idx>=len(b):
        if abs(b[idx-1]-num)<=K:
            return b[idx-1]
        else:
            return -1
    return b[idx]
        
    
        

            
for i in range(N):
    a,c=map(int,input().split())
    m[a]=c
    bisect.insort(b,a)

for i in range(M):
    op=list(map(int,input().split()))
    if op[0]==1:
        m[op[1]]=op[2]
        bisect.insort(b,op[1])
    elif op[0]<=2:
        idx = find_num(op[1])
        if op[0]==2:
            if idx<0:
                continue
        m[idx]=op[2]
    else:
        idx = find_num(op[1])
        if idx<0:
            if idx==-2:
                print('?')
            else:
                print(idx)
        else:
            print(m[idx])
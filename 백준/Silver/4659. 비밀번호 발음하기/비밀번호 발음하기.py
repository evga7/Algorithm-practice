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
dx=[0,1,0,-1,-1,-1,1,1]
dy=[1,0,-1,0,-1,1,1,-1]
def chk(s):
    f=0
    m_cnt=0
    j_cnt=0
    for i,cur in enumerate(s):
        if i-1>=0:
            if cur!='e' and cur!='o':
                if s[i]==s[i-1]:
                    return False
        if cur=='a' or cur=='e' or cur=='i' or cur=='o' or cur=='u':
            f=1
            m_cnt+=1
            j_cnt=0
        else:
            j_cnt+=1
            m_cnt=0
        if m_cnt>=3 or j_cnt>=3:
            return False
    if not f:
        return False
    return True

while True:
    s=input()
    if s=="end":
        break
    print("<"+s+"> is",end=' ')
    if not chk(s):
        print("not",end=' ')
    print("acceptable.")
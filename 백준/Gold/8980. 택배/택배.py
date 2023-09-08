# N,M=map(int,input().split())
# visited=[[987654321]*M for _ in range(N)]
# arr=[list(map(int,input().strip())) for _ in range(N)]
# str=re.findall(r'\d+',str) 숫자만 때기
# re.findall(r'-?\d+', str1)] 음수는 이렇게
# word1 = re.findall("[a-zA-Z]+", st) 이건 문자 추출
#arr2 = [k[::-1] for k in zip(*arr)] 문자열 90도 회전
import bisect
import math
import re

import itertools
import collections
#sys.setrecursionlimit(10 ** 6)
from collections import *
from functools import cmp_to_key
dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M

import sys
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize

def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
N,C=map(int,input().split())
M=int(input())
a=[list(map(int,input().split())) for _ in range(M)]
a.sort(key=lambda x:x[1])
b=[0 for _ in range(N+1)]
res=0
for cur,nxt,cost in a:
    mi=cost
    for i in range(cur,nxt):
        mi=min(mi,C-b[i])
    res+=mi
    for i in range(cur,nxt):
        b[i]+=mi
print(res)
    
    
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
N,M=map(int,input().split())
chk = [[-1 for _ in range(M + 1)] for _ in range(N + 1)]
res=0
m={'R':0,'U':1,'L':2,'D':3}
def go(sx,sy,pos):
    global res
    q=deque()
    q.append((sx,sy))
    while q:
        x,y=q.popleft()
        idx=m[a[x][y]]
        n_x=x+dx[idx]
        n_y=y+dy[idx]
        if chk[n_x][n_y]!=-1:
            if chk[n_x][n_y]==pos:
                res+=1
            return 0
        chk[x][y]=pos
        q.append((n_x,n_y))
    return 0
a=[list(input()) for _ in range(N)]
pos=1
for i in range(N):
    for j in range(M):
        if chk[i][j]==-1:
            go(i,j,pos)
            pos+=1
            
print(res)
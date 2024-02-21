# N,M=map(int,input().split())
# visited=[[987654321]*M for _ in range(N)]
# arr=[list(map(int,input().strip())) for _ in range(N)]
# str=re.findall(r'\d+',str) 숫자만 때기
# re.findall(r'-?\d+', str1)] 음수는 이렇게
# word1 = re.findall("[a-zA-Z]+", st) 이건 문자 추출
#arr2 = [k[::-1] for k in zip(*arr)] 문자열 90도 회전
# p=[i for i in range(N+1)]
# def find(x):
#     if x==p[x]:
#         return x
#     p[x]=find(p[x])
#     return p[x]
# def uni(x,y):
#     x=find(x)
#     y=find(y)
#     if x!=y:
#         if x<y:
#             p[y]=x
#         else:
#             p[x]=y
#         return True
#     return False
import bisect

import re

import itertools
import collections
#sys.setrecursionlimit(10 ** 6)

from functools import cmp_to_key
from typing import List

dx = [0,0,-1,1]  # 오 왼 위 아
dy = [1,-1,0,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
# sys.setrecursionlimit(100000)
import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=[list(input()) for _ in range(N)]
res=0
def chk():
    r=0
    for i in range(N):
        cnt=1
        for j in range(1,N):
            if a[i][j]==a[i][j-1]:
                cnt+=1
                r=max(r,cnt)
            else:
                cnt=1
    for i in range(N):
        cnt=1
        for j in range(1,N):
            if a[j][i]==a[j-1][i]:
                cnt+=1
                r = max(r, cnt)
            else:
                cnt=1
    return r
for i in range(N):
    for j in range(N):
        if j+1<N and a[i][j]!=a[i][j+1]:
            a[i][j],a[i][j+1]=a[i][j+1],a[i][j]
            res=max(res,chk())
            a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
        if i+1<N and a[i][j]!=a[i+1][j]:
            a[i][j],a[i+1][j]=a[i+1][j],a[i][j]
            res=max(res,chk())
            a[i][j],a[i+1][j]=a[i+1][j],a[i][j]
print(res)
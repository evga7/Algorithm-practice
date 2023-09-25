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
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
v=[]
res1=0
res2=0
p=[i for i in range(N+1)]
def find(x):
    if p[x]==x:
        return x
    p[x]=find(p[x])
    return p[x]
def uni(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        if x<y:
            p[y]=x
        else:
            p[x]=y
        return True
    return False
for i in range(M+1):
    a,b,c=map(int,input().split())
    v.append((c,a,b))
v.sort()
cnt=0
cnt2=0
for a,x,y in v:
    c = uni(x, y)
    if not a and c:
        cnt+=1
p=[i for i in range(N+1)]
v.sort(key=lambda x:-x[0])
for a,x,y in v:
    c = uni(x, y)
    if not a and c:
        cnt2+=1
print(pow(cnt,2)-pow(cnt2,2))
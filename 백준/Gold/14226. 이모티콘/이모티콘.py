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
#dx = [0,-1,0,1]  # 오 위 왼 아
#dy = [1,0,-1,0]
dx=[1,1,1,0,0,0,-1,-1,-1]
dy=[-1,0,1,-1,0,1,-1,0,1]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
import sys
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize


def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
N=int(input())
st=set()
q=deque()
q.append((0,1,0))
while q:
    cost,pos,cpy=q.popleft()
    if pos==N:
        print(cost)
        exit(0)
    if pos+cpy<=1000 and not (pos+cpy,cpy) in st:
        st.add((pos+cpy,cpy))
        q.append((cost+1,pos+cpy,cpy))
    if pos-1>=2 and not pos -1 in st:
        st.add(pos -1)
        q.append((cost + 1, pos -1,cpy))
    if not (pos,pos) in st:
        st.add((pos,pos))
        q.append((cost+1,pos,pos))
    

    
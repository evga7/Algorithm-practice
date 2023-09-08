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
N=int(input())
a=list(map(int,input().split()))
dp=[[-1 for _ in range(101)] for _ in range(21)]
def go(num,idx):
    if not (0<=num<=20):
        return 0
    if idx==N-1:
        if num==a[N-1]:
            return 1
        return 0
    if dp[num][idx]!=-1:
        return dp[num][idx]
    dp[num][idx] = 0
    dp[num][idx]+=go(num+a[idx],idx+1)+go(num-a[idx],idx+1)
    return dp[num][idx]

print(go(a[0],1))
    
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
import heapq
import sys
from collections import *
import itertools
import collections
si=sys.stdin.readline
#sys.setrecursionlimit(10 ** 6)
dx = [0,-1,0,1]  # 왼 위 오 아래
dy = [-1,0,1,0]
m=int(1e9)+7
def input():return sys.stdin.readline().rstrip()
N=int(input())
dp=[0 for _ in range(1000001)]
dp[1]=1
dp[2]=1
if N<3:
    print(dp[N])
    exit(0)
res=2
for i in range(3,N+1):
    dp[i]=(dp[i-2]%m+dp[i-1]%m)%m
print(dp[N])





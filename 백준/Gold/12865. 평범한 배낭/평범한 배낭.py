# N,M=map(int,input().split())
# visited=[[987654321]*M for _ in range(N)]
# arr=[list(map(int,input().strip())) for _ in range(N)]
# str=re.findall(r'\d+',str) 숫자만 때기
# re.findall(r'-?\d+', str1)] 음수는 이렇게
# word1 = re.findall("[a-zA-Z]+", st) 이건 문자 추출
import re
import heapq
import sys
from collections import *
import itertools
import collections

sys.setrecursionlimit(10 ** 5)
dx = [0, 1, 0, -1]  # 오 아래 왼 위
dy = [1, 0, -1, 0]
dp=[[-1 for _ in range(100001)]for _ in range(101)]
wv=[]
N,M=map(int,sys.stdin.readline().rstrip().split())
for i in range(N):
    wv.append(list(map(int,sys.stdin.readline().rstrip().split())))

def go(cnt,wei):
    if cnt>=N:
        return 0
    if dp[cnt][wei]!=-1:
        return dp[cnt][wei]
    dp[cnt][wei]=go(cnt+1,wei)
    if wei-wv[cnt][0]>=0:
        dp[cnt][wei]=max(dp[cnt][wei],go(cnt+1,wei-wv[cnt][0])+wv[cnt][1])
    return dp[cnt][wei]

print(go(0,M))





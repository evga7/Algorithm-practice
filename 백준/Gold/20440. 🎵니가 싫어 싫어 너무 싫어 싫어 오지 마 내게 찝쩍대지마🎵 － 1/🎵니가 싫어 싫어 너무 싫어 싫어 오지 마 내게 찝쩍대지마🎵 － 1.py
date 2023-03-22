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
#sys.setrecursionlimit(10 ** 5)
dx = [0,-1,0,1]  # 왼 위 오 아래
dy = [-1,0,1,0]
def input():return sys.stdin.readline().rstrip()
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
arr.sort()
m=defaultdict(int)
for cur in arr:
    s=cur[0]
    e=cur[1]
    m[s]+=1
    m[e]-=1
cnt=0
res=0
res1=0
res2=0
f=0
for cur in sorted(m.keys()):
    cnt+=m[cur]
    if cnt>res:
        res=cnt
        res1=cur
        f=1
    elif cnt<res and cnt-m[cur]==res and f:
        res2=cur
        f=0
print(res)
print(res1,res2)
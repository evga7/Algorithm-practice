# N,M=map(int,input().split())
# visited=[[987654321]*M for _ in range(N)]
# arr=[list(map(int,input().strip())) for _ in range(N)]
# str=re.findall(r'\d+',str) 숫자만 때기
# re.findall(r'-?\d+', str1)] 음수는 이렇게
# word1 = re.findall("[a-zA-Z]+", st) 이건 문자 추출
#arr2 = [k[::-1] for k in zip(*arr)] 문자열 90도 회전
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
res=0
N=int(si().rstrip())
arr=[list(map(int,si().rstrip().split())) for _ in range(N)]
pq=[]
arr.sort(key = lambda x:x[1])
for cur in arr:
    pay=cur[0]
    day=cur[1]
    if len(pq)<day:
        heapq.heappush(pq,pay)
    else:
        if pq[0] < pay:
            heapq.heappop(pq)
            heapq.heappush(pq,pay)

while pq:
    res+=pq.pop()
print(res)
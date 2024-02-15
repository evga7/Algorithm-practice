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
dx = [0,1,0,-1]  #  오 아래 왼 위
dy = [1,0,-1,0]
res=0
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
resv=[]
arr=[]
for i in range(1,N+1):
    arr.append(i)
idx=M-1
while True:
    resv.append(str(arr[idx]))
    N-=1
    if not N:
        break
    del arr[idx]
    idx+=M-1
    idx%=N
print('<',", ".join(resv),'>',sep='')


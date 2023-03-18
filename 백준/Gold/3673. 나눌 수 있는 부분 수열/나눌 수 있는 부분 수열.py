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
#sys.setrecursionlimit(10 ** 9)
dx = [0,1,0,-1,0,0]  #  오 아래 왼 위
dy = [1,0,-1,0,0,0]
dh=[0,0,0,0,1,-1]
res=0
def input():return sys.stdin.readline().rstrip()


T=int(input())
while T:
    T-=1
    M,N=map(int,input().split())
    arr=list(map(int,input().split()))
    d=[0 for _ in range(N)]
    arr[0]%=M
    for i in range(1,N):
        arr[i]=(arr[i]+arr[i-1])%M
    res=0
    m=defaultdict(int)
    for cur in arr:
        if not cur:
            res+=1
        res+=m[cur]
        m[cur]+=1
    print(res)







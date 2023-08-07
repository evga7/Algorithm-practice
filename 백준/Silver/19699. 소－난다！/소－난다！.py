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
prime=[0 for _ in range(10001)]
INF=sys.maxsize
N,M=map(int,input().split())
a=list(map(int,input().split()))
p=itertools.combinations(a,M)
def e():
    prime[1]=1
    for i in range(2,int(math.sqrt(10000))+1):
        if prime[i]:continue
        for j in range(i*i,10001,i):
            prime[j]=1
e()
res_v=[]
st=set()
for cur in p:
    s=sum(cur)
    if not prime[s] and not s in st:
        st.add(s)
        res_v.append(s)
if res_v:
    res_v.sort()
    print(*res_v)
else:
    print(-1)
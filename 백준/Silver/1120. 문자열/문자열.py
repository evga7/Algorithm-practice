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
res=987654321
def input():return sys.stdin.readline().rstrip()
s1,s2=input().split()
for i in range(len(s2)-len(s1)+1):
    idx=i
    cnt=0
    for j in range(len(s1)):
        if s2[idx]!=s1[j]:
            cnt+=1
        idx+=1
    res=min(res,cnt)
print(res)



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
def input():return sys.stdin.readline().rstrip()
visited=[987654321 for _ in range(10001)]
N=int(input())
q=deque()
for i in range(N):
    s=input().split()
    if len(s)>1:
        q.append(s[1])
    else:
        if s[0]=="front":
            if q:
                print(q[0])
            else:
                print(-1)
        elif s[0]=="pop":
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif s[0]=="size":
            print(len(q))
        elif s[0]=="empty":
            if q:
                print(0)
            else:
                print(1)
        elif s[0]=="back":
            if q:
                print(q[-1])
            else:
                print(-1)

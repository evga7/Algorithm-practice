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
def input():return sys.stdin.readline().rstrip()
res=0
N=int(input())
M=int(input())
arr=list(map(int,input().split()))
arr.sort()
a=[]
for i in range(1,len(arr)):
    a.append(int(arr[i]-arr[i-1]))
res=sum(a)
a.sort(reverse=True)
for i in range(M-1):
    if len(a)<=i:break
    res-=a[i]
print(res)
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
N=int(input())
arr=list(map(int,input().split()))
sub=arr[1]-arr[0]
cnt=2
res=2
for i in range(N-2):
    if arr[i]<=arr[i+1]<=arr[i+2]:
        cnt=2
    elif arr[i]>=arr[i+1]>=arr[i+2]:
        cnt=2
    else:
        cnt+=1
    res=max(cnt,res)
print(res)
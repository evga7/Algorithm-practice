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
def input():return sys.stdin.readline().rstrip()
N=int(input())
arr=[list(input()) for _ in range(N)]
res=0
def go():
    c=0
    for i in range(N):
        a1=arr[i]
        a2=list(zip(*arr))[i]
        cc=1
        for i in range(1,len(a1)):
            if a1[i]==a1[i-1]:
                cc+=1
                c=max(c,cc)
            else:
                cc=1
        cc=1
        for i in range(1,len(a2)):
            if a2[i]==a2[i-1]:
                cc+=1
                c=max(c,cc)
            else:
                cc=1
    return c
res=max(res,go())
for i in range(N):
    for j in range(N-1):
        cur=arr[i][j]
        if cur!=arr[i][j+1]:
            arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j]
            res=max(res,go())
            arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j]
        if i+1<N and cur!=arr[i+1][j]:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            res=max(res,go())
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
print(res)
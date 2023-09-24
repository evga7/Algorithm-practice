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
dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M

import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
a=[list(input()) for _ in range(N)]
res=0 

def allchk():
    global res
    for i in range(N):
        temp=a[i]
        temp2 = list(zip(*a))[i]
        cnt=1
        cnt2=1
        for j in range(1,N):
            if temp2[j]==temp2[j-1]:
                cnt2+=1
                res=max(res,cnt2)
            else:
                cnt2=1
            if temp[j]==temp[j-1]:
                cnt+=1
                res=max(res,cnt)
            else:
                cnt=1
def chk(x,y,op):
    global res
    if op:
        temp,temp2=a[x],a[x+1]
        temp3 = list(zip(*a))[y]
        cnt=1
        cnt2=1
        cnt3=1
        for i in range(1,N):
            if temp2[i]==temp2[i-1]:
                cnt2+=1
                res=max(res,cnt2)
            else:
                cnt2=1
            if temp[i]==temp[i-1]:
                cnt+=1
                res=max(res,cnt)
            else:
                cnt=1
            if temp3[i]==temp3[i-1]:
                cnt3+=1
                res=max(res,cnt3)
            else:
                cnt3=1
    else:
        temp = list(zip(*a))[y+1]
        temp2 = list(zip(*a))[y]
        temp3=a[x]
        cnt=1
        cnt2=1
        cnt3=1
        for i in range(1,N):
            if temp2[i]==temp2[i-1]:
                cnt2+=1
                res=max(res,cnt2)
            else:
                cnt2=1
            if temp[i]==temp[i-1]:
                cnt+=1
                res=max(res,cnt)
            else:
                cnt=1
            if temp3[i]==temp3[i-1]:
                cnt3+=1
                res=max(res,cnt3)
            else:
                cnt3=1
    
def go(x,y):
    if y+1<N and a[x][y]!=a[x][y+1]:
        a[x][y],a[x][y+1]=a[x][y+1],a[x][y]
        chk(x,y,0)
        a[x][y], a[x][y + 1] = a[x][y + 1], a[x][y]
    if x+1<N and a[x][y]!=a[x+1][y]:
        a[x][y], a[x+1][y] = a[x+1][y], a[x][y]
        chk(x,y,1)
        a[x][y], a[x+1][y] = a[x+1][y], a[x][y]
allchk()
for i in range(N):
    for j in range(N):
        go(i,j)
print(res)
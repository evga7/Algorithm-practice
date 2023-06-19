# N,M=map(int,input().split())
# visited=[[987654321]*M for _ in range(N)]
# arr=[list(map(int,input().strip())) for _ in range(N)]
# str=re.findall(r'\d+',str) 숫자만 때기
# re.findall(r'-?\d+', str1)] 음수는 이렇게
# word1 = re.findall("[a-zA-Z]+", st) 이건 문자 추출
#arr2 = [k[::-1] for k in zip(*arr)] 문자열 90도 회전
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
N=int(si().rstrip())
res=-float('inf')
res2=float('inf')
arr=list(map(int,si().rstrip().split()))
p,s,m,d=map(int,si().rstrip().split())
def go(idx,plus,sub,mul,div,s):
    if idx==N:
        global res,res2
        res=max(s,res)
        res2=min(res2,s)
        return
    if plus:
        go(idx+1,plus-1,sub,mul,div,s+arr[idx])
    if sub:
        go(idx+1,plus,sub-1,mul,div,s-arr[idx])
    if mul:
        go(idx+1,plus,sub,mul-1,div,s*arr[idx])
    if div and arr[idx]:
        go(idx+1,plus,sub,mul,div-1,int(s/arr[idx]))

go(1,p,s,m,d,arr[0])
print(res)
print(res2)




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
N,M,T=map(int,input().split())
graph=[]
parent=[i for i in range(N+1)]
res=0
for i in range(M):
    a,b,c=map(int,input().split())
    graph.append((c,a,b))
graph.sort()

def find(x):
    if x==parent[x]:
        return x
    parent[x]=find(parent[x])
    return parent[x]
def uni(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        parent[y]=x
        return True
    return False
cnt=0
for cur in graph:
    cost=cur[0]
    x=cur[1]
    y=cur[2]
    if uni(x,y):
        res+=cost+(cnt*T)
        cnt+=1

print(res)
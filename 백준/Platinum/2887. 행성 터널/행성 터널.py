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
# p = [i for i in range(N + 1)]
# def find(x):
#     if p[x] == x:
#         return x
#     p[x] = find(p[x])
#     return p[x]
# def uni(x, y):
#     x = find(x)
#     y = find(y)
#     if x != y:
#         if x < y:
#             p[y] = x
#         else:
#             p[x] = y
#         return True
#     return False
#dx = [-1,0]  # 오 왼 위 아
#dy = [0,-1]
import heapq
import itertools
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)+7
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
#dx=[0,1,0,-1,-1,-1,1,1]
#dy=[1,0,-1,0,-1,1,1,-1]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
N=int(input())
a=[]
b=[]
c=[]
p = [i for i in range(N + 1)]
def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]
def uni(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if x < y:
            p[y] = x
        else:
            p[x] = y
        return True
    return False

for i in range(N):
    q,w,e=map(int,input().split())
    a.append((q,i+1))
    b.append((w, i+1))
    c.append((e, i+1))
a.sort()
b.sort()
c.sort()
v=[]
for i in range(1,N):
    v.append((a[i][0]-a[i-1][0],a[i][1],a[i-1][1]))
    v.append((b[i][0] - b[i - 1][0], b[i][1], b[i-1][1]))
    v.append((c[i][0] - c[i - 1][0], c[i][1], c[i-1][1]))
v.sort()
res=0
for cost,S,E in v:
    if uni(S,E):
        res+=cost
print(res)
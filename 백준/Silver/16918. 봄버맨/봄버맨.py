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
N,M,R=map(int,input().split())
a=[list(input()) for _ in range(N)]
c=[[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        if a[i][j]=='O':
            c[i][j]=2
t=1
def boom():
    v=[]
    for i in range(N):
        for j in range(M):
            if c[i][j]:
                c[i][j]-=1
            if not c[i][j]:
                v.append((i,j))
    for x,y in v:
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M):
                c[n_x][n_y]=0
                
def bomb():
    for i in range(N):
        for j in range(M):
            if c[i][j]:continue
            c[i][j]=4
while t<R:
    bomb()
    boom()
    t+=1
for i in range(N):
    for j in range(M):
        if c[i][j]:
            print('O',end='')
        else:
            print('.',end='')
    print('')
print('')

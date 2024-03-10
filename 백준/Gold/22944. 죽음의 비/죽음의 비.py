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
N,H,D=map(int,input().split())
arr=[input() for _ in range(N)]
sx=0
sy=0
res=-1
visited=[[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if arr[i][j]=='S':
            sx=i
            sy=j

q=deque()
q.append((sx,sy,H,0,0))
while q:
    x,y,h,d,cost=q.popleft()
    if not h:
        continue
    if arr[x][y]=='E':
        res=cost
        break
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if 0<=n_x<N and 0<=n_y<N:
            if arr[n_x][n_y]=='.':
                if d:
                    if visited[n_x][n_y]<h:
                        visited[n_x][n_y]=h
                        q.append((n_x,n_y,h,d-1,cost+1))
                elif h:
                    if visited[n_x][n_y]<h-1:
                        visited[n_x][n_y]=h-1
                        q.append((n_x, n_y, h-1, d, cost + 1))
            elif arr[n_x][n_y]=='U':
                if visited[n_x][n_y] <h:
                    visited[n_x][n_y] = h
                    q.append((n_x,n_y,h,D-1,cost+1))
            elif arr[n_x][n_y]=='E':
                q.append((n_x,n_y,h,d,cost+1))
print(res)
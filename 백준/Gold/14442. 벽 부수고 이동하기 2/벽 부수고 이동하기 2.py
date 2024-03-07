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
res=0
def input():return sys.stdin.readline().rstrip()
N,M,K=map(int,input().split())
arr=[list(map(int,input())) for _ in range(N)]
visited=[[[987654321 for _ in range(11)] for _ in range(M+1)] for _ in range(N+1)]
q=deque()
q.append((0,0,K,1))
while q:
    x,y,block,cost=q.popleft()
    if x==N-1 and y==M-1:
        print(cost)
        exit(0)
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if 0<=n_x<N and 0<=n_y<M:
            nxt=arr[n_x][n_y]
            if nxt==0:
                if visited[n_x][n_y][block]>cost+1:
                    visited[n_x][n_y][block] = cost + 1
                    q.append((n_x,n_y,block,cost+1))
            else:
                if block:
                    if visited[n_x][n_y][block-1] > cost + 1:
                        visited[n_x][n_y][block-1] = cost + 1
                        q.append((n_x,n_y,block-1,cost+1))
print(-1)
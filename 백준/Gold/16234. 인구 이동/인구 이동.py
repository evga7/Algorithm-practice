# N,M=map(int,input().split())
# visited=[[987654321]*M for _ in range(N)]
# arr=[list(map(int,input().strip())) for _ in range(N)]
# str=re.findall(r'\d+',str) 숫자만 때기
# re.findall(r'-?\d+', str1)] 음수는 이렇게
# word1 = re.findall("[a-zA-Z]+", st) 이건 문자 추출
import re
import heapq
import sys
from collections import *
import itertools
sys.setrecursionlimit(10 ** 5)
dx = [-1, 1, 0, 0]  # 위 아래 왼 오
dy = [0, 0, -1, 1]
arr=[]
open=[[0]*51 for _ in range(51)]
visited=[[0]*51 for _ in range(51)]
N,L,R=map(int,input().split())
for i in range(N):
    arr.append(list(map(int,input().split())))
f=0
res=0
s=0
pos=[]
def go2(x,y):
    global pos
    global s
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    while q:
        cur_x,cur_y=q.popleft()
        pos.append((cur_x,cur_y))
        s+=arr[cur_x][cur_y]
        for i in range(4):
            n_x=cur_x+dx[i]
            n_y=cur_y+dy[i]
            if 0<=n_x<N and 0<=n_y<N and not visited[n_x][n_y]:
                sub=abs(arr[cur_x][cur_y]-arr[n_x][n_y])
                if L<=sub<=R:
                    visited[n_x][n_y]=1
                    q.append((n_x,n_y))
def go():
    global f
    global s
    global pos
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                go2(i,j)
                cost=s//len(pos)
                for cur in pos:
                    if cost!=arr[cur[0]][cur[1]]:
                        arr[cur[0]][cur[1]]=cost
                        f=1
                pos=[]
                s=0


while 1:
    visited = [[0] * 51 for _ in range(51)]
    go()
    if not f:
        break
    pos=[]
    res+=1
    s=0
    f=0


print(res)
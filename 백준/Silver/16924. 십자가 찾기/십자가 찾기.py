dx = [1, -1, 0, 0]  # 아 위 오 왼
dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M


import copy
import bisect
import sys
import heapq
from collections import *
#sys.setrecursionlimit(100000)
N,M=map(int,input().split())
a=[list(input()) for _ in range(N)]
m=min(N,M)
chked=[[0 for _ in range(M+1)] for _ in range(N+1)]
def go(x,y,c):
    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]
        cnt = 0
        while is_inside(n_x, n_y, N, M) and a[n_x][n_y] == '*':
            cnt += 1
            n_x += dx[i]
            n_y += dy[i]
        if cnt<c:
            return False
            
            
    return True
            
        
    
res_v=[]
def ccccc(x,y,cnt):
    chked[x][y]=1
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        c=0
        while c<cnt:
            chked[n_x][n_y]=1
            c+=1
            n_x+=dx[i]
            n_y+=dy[i]
for i in range(1,N):
    for j in range(1,M):
        if a[i][j]=='*':
            for k in range(m+1,0,-1):
                l=0
                if go(i,j,k):
                    l=k
                    break
            if l>0:
                ccccc(i,j,l)
                for k in range(1,l+1):
                    res_v.append((i+1,j+1,k))
for i in range(N):
    for j in range(M):
        if a[i][j]=='*' and not chked[i][j]:
            print(-1)
            exit(0)
print(len(res_v))
for cur in res_v:
    print(cur[0],cur[1],cur[2])
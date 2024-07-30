dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]
#dx = [0,1,0,-1]  # 오 아 왼 위
#dy = [1,0,-1,0]
dd=[0,4,2,4,4,1]
import heapq
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import copy
from collections import *
import bisect
# sys.setrecursionlimit(100000)
import sys
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
a=[input() for _ in range(N)]
b=[input() for _ in range(N)]
flag=0
c=[]
for i in range(N):
    s=""
    for j in range(N):
        if b[i][j]=='x' and a[i][j]=='.':
            cnt=0
            for k in range(8):
                n_x=i+dx[k]
                n_y=j+dy[k]
                if is_inside(n_x,n_y,N,N):
                    if a[n_x][n_y]=='*':
                        cnt+=1
            s+=str(cnt)
        elif b[i][j]=='x' and a[i][j]=='*':
            flag=1
            s+='*'
        else:
            s+=str(b[i][j])
    c.append(s)
for i in range(N):
    for j in range(N):
        if flag and a[i][j]=='*':
            print('*',end='')
        else:
            print(c[i][j],end='')
    print('')
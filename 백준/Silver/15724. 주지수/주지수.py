import heapq
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
b=[[0 for _ in range(M+1)] for _ in range(N+1)]
T=int(input())
for i in range(1,N+1):
    for j in range(1,M+1):
        b[i][j]=a[i-1][j-1]+b[i-1][j]+b[i][j-1]-b[i-1][j-1]
for i in range(T):
    x1,y1,x2,y2=map(int,input().split())
    print(b[x2][y2]-b[x2][y1-1]-b[x1-1][y2]+b[x1-1][y1-1])
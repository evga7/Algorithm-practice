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
a=[int(input()) for _ in range(N)]
left=0
right=int(1e21)
while left<=right:
    mid=left+right>>1
    cnt=0
    for cur in a:
        cnt+=mid//cur
    if cnt>=M:
        right=mid-1
    else:
        left=mid+1
print(left)

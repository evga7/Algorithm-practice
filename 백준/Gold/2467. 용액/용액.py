from collections import *
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
#dx = [0, 0, 1, -1]
#dy = [1, -1, 0, 0]
dx=[1,1,1]
dy=[-1,0,1]
N=int(input())
a=list(map(int,input().split()))
left=0
right=N-1
res=int(1e10)
res_left=0
res_right=0
while left<right:
    s=a[left]+a[right]
    if abs(s)<res:
        res=abs(s)
        res_left=a[left]
        res_right = a[right]
    if s>=0:
        right-=1
    else:
        left+=1
print(res_left,res_right)
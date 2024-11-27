from collections import *
import bisect
import re
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1,-1]
dy = [1, -1, 0, 0]
N=int(input())
s=input()
left=0
right=1
m=defaultdict(int)
m[s[0]]+=1
res=0
l=1
L=len(s)
while left<right and right<L:
    while left<right and l>N:
        m[s[left]]-=1
        if m[s[left]]==0:
            l-=1
            del m[s[left]]
        left+=1
    if not s[right] in m:
        l+=1
    if l<=N:
        res=max(res,right-left+1)
    m[s[right]]+=1
    right+=1
print(res)
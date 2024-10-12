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
s=input()
ss="wolf"
idx=0
if s[0]!='w' or s[-1]!='f':
    print(0)
    exit(0)
cnt=0
v=[]
for i in range(len(s)):
    if ss[idx]==s[i]:
        cnt+=1
    else:
        v.append(cnt)
        cnt=1
        idx+=1
        idx%=4
        if ss[idx]!=s[i]:
            print(0)
            exit(0)
if cnt:
    v.append(cnt)
cnt2=0
for i in range(len(v)):
    if not i%4:
        cnt2=v[i]
    else:
        if cnt2!=v[i]:
            print(0)
            exit(0)
print(1)
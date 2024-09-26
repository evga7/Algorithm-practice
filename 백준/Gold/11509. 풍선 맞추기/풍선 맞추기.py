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
N=int(input())
a=list(map(int,input().split()))
m=defaultdict(int)
res=0
for cur in a:
    if cur+1 in m:
        m[cur+1]-=1
        if not m[cur+1]:
            del m[cur+1]
    else:
        res+=1
    m[cur] += 1
print(res)

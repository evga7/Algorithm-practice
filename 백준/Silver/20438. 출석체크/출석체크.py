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
N,K,Q,M=map(int,input().split())
a=set(map(int,input().split()))
b=list(map(int,input().split()))
c=[0 for _ in range(50001)]
for cur in b:
    if cur in a:continue
    cc=cur
    while cc<=50000:
        c[cc]=1
        cc+=cur
for cur in a:
    c[cur]=0
d=[0 for _ in range(50001)]
for i in range(1,50001):
    d[i]=d[i-1]
    if not c[i]:
        d[i]+=1
for i in range(M):
    S,E=map(int,input().split())
    print(d[E]-d[S-1])


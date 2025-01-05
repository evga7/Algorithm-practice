import bisect
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
N,M=map(int,input().split())
a=list(map(int,input().split()))
res=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            s=a[i]+a[j]+a[k]
            if s<=M and s>res:
                res=s
print(res)
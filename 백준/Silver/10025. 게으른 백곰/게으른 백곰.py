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
a.sort(key=lambda x:x[1])
left=0
right=0
s=0
res=0
while left<=right and right<N:
    if a[right][1]-a[left][1]<=M*2:
        s+=a[right][0]
        res=max(res,s)
        right+=1
    else:
        s-=a[left][0]
        left+=1
print(res)
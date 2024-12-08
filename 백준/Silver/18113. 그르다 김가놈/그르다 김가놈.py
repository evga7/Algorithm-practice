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
N,K,M=map(int,input().split())
a=[]
for i in range(N):
    num=int(input())
    if num>K:
        a.append(num)
left=1
right=int(1e9)
while left<=right:
    mid=left+right>>1
    cnt=0
    for cur in a:
        s=cur
        tk=2*K
        if tk<=cur:
            s-=tk
        else:
            s-=K
        cnt+=s//mid
    if cnt>=M:
        left=mid+1
    else:
        right=mid-1
if left==1:
    left=0
print(left-1)
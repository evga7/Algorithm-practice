import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
M=int(input())
left=0
right=min(N*N,int(1e10))
def chk(mid):
    cnt=0
    for i in range(1,N+1):
        cnt+=min(mid//i,N)
    return cnt
while left<=right:
    mid=left+right>>1
    if chk(mid)>=M:
        right=mid-1
    else:
        left=mid+1
print(left)
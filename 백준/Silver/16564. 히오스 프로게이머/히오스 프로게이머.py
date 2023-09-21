import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
a=[int(input()) for _ in range(N)]
left=0
right=int(1e17)
while left<=right:
    mid=left+right>>1
    cnt=0
    for cur in a:
        if cur>=mid:continue
        cnt+=mid-cur
    if cnt<=M:
        left=mid+1
    else:
        right=mid-1
print(left-1)
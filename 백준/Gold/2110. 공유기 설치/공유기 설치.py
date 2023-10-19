import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
a=[int(input()) for _ in range(N)]
left=0
right=int(1e16)
a.sort()
while left<=right:
    mid=left+right>>1
    cnt=1
    back=a[0]
    for i in range(1,N):
        if a[i]-back<mid:continue
        back=a[i]
        cnt+=1
    if cnt<M:
        right=mid-1
    else:
        left=mid+1
print(left-1)
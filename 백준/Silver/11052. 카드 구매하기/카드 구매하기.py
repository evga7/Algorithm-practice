import sys
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
a=list(map(int,input().split()))
dp=[[-1 for _ in range(N+1)] for _ in range(N+1)]
def go(idx,cnt):
    if idx==N:
        if cnt==N:
            return 0
        return -987654321
    if dp[idx][cnt]!=-1:
        return dp[idx][cnt]
    ret=0
    cur=a[idx]
    num=idx+1
    ret=max(ret,go(idx+1,cnt))
    for i in range(1,N+1):
        if cnt+(i*num)<=N:
            ret=max(ret,go(idx+1,cnt+(i*num))+(i*cur))
    dp[idx][cnt]=ret
    return dp[idx][cnt]
print(go(0,0))
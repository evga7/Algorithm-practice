import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=[int(input()) for _ in range(N)]
dp=[[-1 for _ in range(N+1)] for _ in range(4)]
def go(cnt,idx):
    if idx>=N or cnt>=3:
        return -987654321
    if dp[cnt][idx]!=-1:
        return dp[cnt][idx]
    if idx==N-1:
        return a[idx]
    ret=0
    ret=max(ret,go(cnt+1,idx+1)+a[idx],go(1,idx+2)+a[idx])
    dp[cnt][idx]=ret
    return dp[cnt][idx]
print(max(go(1,0),go(1,1)))
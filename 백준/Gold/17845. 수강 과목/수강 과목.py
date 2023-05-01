import sys
def input():return sys.stdin.readline().rstrip()
N,K=map(int,input().split())
dp=[[-1 for _ in range(10001)] for _ in range(1001)]
a=[list(map(int,input().split())) for _ in range(K)]
def go(idx,s):
    if idx==K:
        return 0
    if dp[idx][s]!=-1:
        return dp[idx][s]
    ret=0
    if a[idx][1]+s<=N:
        ret=max(ret,go(idx+1,s+a[idx][1])+a[idx][0])
    ret=max(ret,go(idx+1,s))
    dp[idx][s]=ret
    return dp[idx][s]
print(go(0,0))
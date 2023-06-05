import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
dp=[[-1 for _ in range(N+2)] for _ in range(2)]
def go(op,idx):
    if idx>=N:
        return 0
    if dp[op][idx]!=-1:
        return dp[op][idx]
    ret=0
    ret=max(ret,go(0,idx+1))
    for i in range(idx,N):
        ret=max(ret,go(1,i+1)+abs(a[idx]-a[i]))
    dp[op][idx]=ret
    return dp[op][idx]
print(go(0,0))
import sys
def input():return sys.stdin.readline().rstrip()
prime=[0 for _ in range(10001)]
INF=sys.maxsize
N=int(input())
M=int(input())
a=[0 for _ in range(N+1)]
for i in range(M):
    num=int(input())
    a[num-1]=1
dp=[-1 for _ in range(N+1)]
def go(idx):
    if idx>=N-1:
        return 1
    if dp[idx]!=-1:
        return dp[idx]
    ret=0
    if a[idx]:
        return go(idx+1)
    if a[idx+1]:
        ret+=go(idx+1)
    else:
        ret+=go(idx+1)+go(idx+2)
    dp[idx]=ret
    return dp[idx]

print(go(0))
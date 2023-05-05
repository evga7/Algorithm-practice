import sys
def input():return sys.stdin.readline().rstrip()
dp=[-1 for _ in range(1001)]
def go(idx):
    if idx<0:
        return 0
    if idx==0:
        return 1
    if dp[idx]!=-1:
        return dp[idx]
    ret=0
    ret+=(go(idx-2)*2+go(idx-1))%10007
    dp[idx]=ret
    return dp[idx]
N=int(input())
print(go(N))
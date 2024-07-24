import sys
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N,M,K=map(int,input().split())
a=[int(input()) for _ in range(N)]
dp=[-1 for _ in range(N+1)]
def go(idx):
    if idx==N:
        return 0
    if dp[idx]!=-1:
        return dp[idx]
    ret=MAX
    mi=MAX
    mx=0
    for i in range(idx,min(idx+M,N)):
        mx=max(mx,a[i])
        mi=min(mi,a[i])
        su=mx-mi
        num=i-idx+1
        ret=min(ret,go(i+1)+K+num*su)
    dp[idx]=ret
    return dp[idx]
print(go(0))


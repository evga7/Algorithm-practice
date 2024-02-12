import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
dp=[-1 for _ in range(N+1)]
def go(idx):
    if idx<0:
        return 987654321
    if idx==0:
        return 0
    if dp[idx]!=-1:
        return dp[idx]
    ret=987654321
    ret=min(ret,go(idx-3)+1,go(idx-5)+1)
    dp[idx]=ret
    return dp[idx]
res=go(N)
if res==987654321:
    res=-1
print(res)
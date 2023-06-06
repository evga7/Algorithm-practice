import sys
sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[int(input()) for _ in range(N)]
dp=[-1 for _ in range(M+1)]
def go(pos):
    if pos==M:
        return 0
    if dp[pos]!=-1:
        return dp[pos]
    ret=987654321
    for i in range(N):
        if pos+a[i]<=M:
            ret=min(ret,go(pos+a[i])+1)
    dp[pos]=ret
    return dp[pos]
res=go(0)
if res==987654321:
    res=-1
print(res)
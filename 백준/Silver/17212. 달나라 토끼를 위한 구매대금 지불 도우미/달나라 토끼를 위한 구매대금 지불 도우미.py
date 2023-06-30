import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
dp = [-1 for _ in range(N + 1)]
a=[1,2,5,7]
def go(idx):
    if idx == N:
        return 0
    if dp[idx] != -1:
        return dp[idx]
    ret=987654321
    for i in range(4):
        if idx+a[i]<=N:
            ret=min(ret,go(idx+a[i])+1)
    dp[idx]=ret
    return dp[idx]
print(go(0))
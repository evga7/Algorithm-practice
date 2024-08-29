import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
dp=[-1 for _ in range(N+1)]
def go(idx):
    if idx<=1:
        return 1
    if dp[idx]!=-1:
        return dp[idx]

    ret=0
    for i in range(idx):
        ret+=go(idx-i-1)*go(i)
    dp[idx]=ret
    return dp[idx]
print(go(N))
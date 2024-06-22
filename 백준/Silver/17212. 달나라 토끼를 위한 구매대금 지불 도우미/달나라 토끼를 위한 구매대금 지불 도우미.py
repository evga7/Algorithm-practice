import sys
sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
a=[7,5,2,1]
N=int(input())
dp=[-1 for _ in range(100001)]
def solve(idx):
    if idx==0:
        return 0
    if dp[idx]!=-1:
        return dp[idx]
    ret=987654321
    for cur in a:
        if idx-cur>=0:
            ret=min(ret,solve(idx-cur)+1)
    dp[idx]=ret
    return dp[idx]
print(solve(N))
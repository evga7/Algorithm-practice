import sys
sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
T=int(input())
dp=[[-1 for _ in range(100001)] for _ in range(2)]
def go(c,idx):
    if idx==0:
        if c&1:
            return 1
        return 0
    if dp[c][idx]!=-1:
        return dp[c][idx]
    ret=0
    for i in range(1,4):
        if idx-i>=0:
            ret+=go(1-c,idx-i)%MOD
    dp[c][idx]=ret
    return dp[c][idx]%MOD
while T:
    T-=1
    N=int(input())
    print(go(0,N)%MOD,go(1,N)%MOD)
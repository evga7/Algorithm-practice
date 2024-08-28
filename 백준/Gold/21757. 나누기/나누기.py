import itertools
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
a=list(map(int,input().split()))
b=list(itertools.accumulate(a))
dp=[[-1 for _ in range(N)] for _ in range(4)]
if b[-1]%4:
    print(0)
    exit(0)
K=b[-1]//4
def go(cnt,idx):
    if cnt==3:
        if idx<=N-1:
            return 1
        return 0
    if idx==N:
        return 0
    if dp[cnt][idx]!=-1:
        return dp[cnt][idx]
    ret=0
    if b[idx]==(cnt+1)*K:
        ret+=go(cnt+1,idx+1)
    ret+=go(cnt,idx+1)
    dp[cnt][idx]=ret
    return dp[cnt][idx]
print(go(0,0))
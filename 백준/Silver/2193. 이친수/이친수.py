import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
dp=[[-1 for _ in range(2)] for _ in range(91)]
def go(cnt,op):
    if cnt==N:
        return 1
    if dp[cnt][op]!=-1:
        return dp[cnt][op]
    ret=0
    if op==0:
        ret+=go(cnt+1,1)
    ret+=go(cnt+1,0)
    dp[cnt][op]=ret
    return dp[cnt][op]
print(go(1,1))
from collections import *
import sys
def input(): return sys.stdin.readline().rstrip()
dp=defaultdict(int)
N,M=map(int,input().split())
def go(idx):
    if idx==0:
        return 987654321
    if idx==N:
        return 1
    if dp[idx]:
        return dp[idx]
    ret=987654321
    if idx%10==1:
        ret=min(ret,go(idx//10)+1)
    if not idx%2:
        ret=min(ret,go(idx//2)+1)
    dp[idx]=ret
    return dp[idx]
res=go(M)
if res==987654321:
    res=-1
print(res)
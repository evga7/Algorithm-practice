from collections import *
import bisect
import itertools
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
a=list(map(int,input().split()))
b=[0]+list(itertools.accumulate(a))
dp=[[defaultdict(int) for _ in range(N+2)] for _ in range(4)]
def go(cnt,idx,num):
    if cnt>4:
        return 0
    if idx==N+1:
        if cnt==3:
            return 1
        return 0
    if num in dp[cnt][idx]:
        return dp[cnt][idx][num]
    ret=0
    for i in range(idx,N+1):
        if b[i]-b[idx-1]==num:
            ret+=go(cnt+1,i+1,num)
    dp[cnt][idx][num]=ret
    return dp[cnt][idx][num]
res=0
for i in range(1,N-2):
    res+=go(0,i+1,b[i])
print(res)

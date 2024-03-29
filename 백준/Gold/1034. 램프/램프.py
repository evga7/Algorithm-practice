from collections import *
import bisect
# sys.setrecursionlimit(100000)
import sys
def input():
    return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(input()) for _ in range(N)]
K=int(input())
res=0
m=defaultdict(int)
def chk():
    cnt=0
    for k in range(N):
        s = ''.join(a[k])
        if not '0' in s:
            cnt += 1
    return cnt
for i in range(N):
    s=''.join(a[i])
    m[s]+=1
for cur in m.keys():
    c=cur.count('0')
    if c&1 and K&1 and c<=K:
        res=max(res,m[cur])
    elif not c&1 and not K&1 and c<=K:
        res = max(res, m[cur])
print(res)
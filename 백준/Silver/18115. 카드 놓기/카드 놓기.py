from collections import *
import bisect
# sys.setrecursionlimit(100000)
import sys
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
dq=deque()
N=int(input())
a=list(map(int,input().split()))
res=deque()
a.reverse()
for i,cur in enumerate(a):
    if cur==1:
        res.appendleft(i+1)
    elif cur==2:
        res.insert(1,i+1)
    elif cur==3:
        res.append(i+1)
print(*res)
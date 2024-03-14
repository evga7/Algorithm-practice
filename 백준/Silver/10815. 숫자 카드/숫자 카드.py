import sys
import bisect
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
a.sort()
M=int(input())
b=list(map(int,input().split()))
for cur in b:
    idx=bisect.bisect_left(a,cur)
    if N>idx>=0 and a[idx]==cur:
        print(1,end=' ')
    else:
        print(0,end=' ')
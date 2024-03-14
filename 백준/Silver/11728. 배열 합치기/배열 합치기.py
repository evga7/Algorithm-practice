import sys
import bisect
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
idx=0
idx2=0
a.sort()
b.sort()
while idx<N and idx2<M:
    if a[idx]<b[idx2]:
        print(a[idx],end=' ')
        idx+=1
    else:
        print(b[idx2],end=' ')
        idx2+=1
while idx<N:
    print(a[idx],end=' ')
    idx+=1
while idx2<M:
    print(b[idx2],end=' ')
    idx2+=1
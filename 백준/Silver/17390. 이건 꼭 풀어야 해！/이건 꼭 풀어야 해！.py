import sys
import itertools
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
b=[0]+list(itertools.accumulate(a))
for i in range(M):
    s,e=map(int,input().split())
    print(b[e]-b[s-1])
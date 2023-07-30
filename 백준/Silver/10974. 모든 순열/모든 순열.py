import sys
from itertools import *
def input(): return sys.stdin.readline().rstrip()
N=int(input())
v=[]
for i in range(1,N+1):
    v.append(i)
a=permutations(v)
for cur in a:
    for cur2 in cur:
        print(cur2,end=' ')
    print()
from collections import *
import sys
import bisect
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
A=Counter(a)
M=int(input())
b=list(map(int,input().split()))
for cur in b:
    if cur in A:
        print(A[cur],end=' ')
    else:
        print(0,end=' ')
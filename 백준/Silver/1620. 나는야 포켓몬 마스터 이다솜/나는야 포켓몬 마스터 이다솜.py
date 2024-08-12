from collections import *
import bisect
# sys.setrecursionlimit(100000)
import sys
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
dp=[[-1 for _ in range(2001)] for _ in range(2001)]
N,M=map(int,input().split())
m=defaultdict(int)
m2=defaultdict(str)
for i in range(N):
    s=input()
    m[s]=i+1
    m2[i+1]=s
for i in range(M):
    op=input()
    if op.isdigit():
        print(m2[int(op)])
    else:
        print(m[op])
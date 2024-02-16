from collections import *
# sys.setrecursionlimit(100000)
import sys
INF = sys.maxsize
def input():
    return sys.stdin.readline().rstrip()
s=input()
C=Counter(s)
for i in range(26):
    print(C[chr(97+i)],end=' ')
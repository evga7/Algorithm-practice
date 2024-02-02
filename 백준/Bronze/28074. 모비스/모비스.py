from collections import *
import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
s=Counter(input())
if 'M' in s and 'O' in s and 'B' in s and 'I' in s and 'S' in s :
    print("YES")
else:
    print("NO")
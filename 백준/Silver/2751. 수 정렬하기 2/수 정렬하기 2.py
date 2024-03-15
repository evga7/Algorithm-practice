import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[int(input()) for _ in range(N)]
a.sort()
for cur in a:
    print(cur)
import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=list(input())
if '0' not in N:
    print(-1)
    exit(0)
num=0
for cur in N:
    num+=int(cur)
if num%3:
    print(-1)
else:
    N.sort(reverse=True)
    print(''.join(N))
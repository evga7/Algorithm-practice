
import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
for i in range(N-1):
    if i&1:
        print(2,end= ' ')
    else:
        print(1,end=' ')
if N&1:
    print(3)
else:
    print(2)

import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
def chk(num):
    return (num*(num+1))//2
n=chk(M)
if n>N:
    print(-1)
else:
    if (N-n)%M:
        print(M)
    else:
        print(M-1)
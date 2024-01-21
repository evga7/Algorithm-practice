import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
a=[int(input()) for _ in range(N)]
res=0
a.sort()
for i in range(N):
    res=max(res,a[i],(a[i])*(N-i))
print(res)
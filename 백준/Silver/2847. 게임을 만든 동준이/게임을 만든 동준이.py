import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
#map(int,input().split())
INF=sys.maxsize
N=int(input())
a=[int(input()) for _ in range(N)]
a.reverse()
b=[987654321 for _ in range(N+1)]
for i in range(1,N+1):
    b[i]=min(b[i-1]-1,a[i-1])


res=0
for i in range(1,N+1):
    res+=abs(a[i-1]-b[i])
print(res)
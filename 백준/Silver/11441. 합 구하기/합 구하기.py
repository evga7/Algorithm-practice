import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
a=list(map(int,input().split()))
M=int(input())
s=[0 for _ in range(N+1)]
for i in range(1,N+1):
    s[i]=s[i-1]+a[i-1]
for i in range(M):
    a,b=map(int,input().split())
    print(s[b]-s[a-1])

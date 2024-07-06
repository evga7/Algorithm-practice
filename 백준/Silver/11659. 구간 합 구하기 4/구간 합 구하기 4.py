import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N,M=map(int,input().split())
a=list(map(int,input().split()))
b=[0 for _ in range(N+1)]
for i in range(1,N+1):
    b[i]=b[i-1]+a[i-1]
for i in range(M):
    s,e=map(int,input().split())
    print(b[e]-b[s-1])
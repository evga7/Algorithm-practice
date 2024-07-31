import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N,M=map(int,input().split())
a=[0]+list(map(int,input().split()))
b=[0]+list(map(int,input().split()))
while M:
    M-=1
    c=[0 for _ in range(N+1)]
    for i in range(1,N+1):
        S,D=a[i],b[i]
        c[D]=S
    a=c[:]
print(*a[1:])
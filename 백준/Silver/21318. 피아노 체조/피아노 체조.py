import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
b=[0 for _ in range(N+1)]
M=int(input())
for i in range(1,N):
    b[i]=b[i-1]
    if a[i]<a[i-1]:
        b[i]+=1
for i in range(M):
    c,d=map(int,input().split())
    print(b[d-1]-b[c-1])
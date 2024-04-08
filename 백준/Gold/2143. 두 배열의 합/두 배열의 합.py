from collections import *
T=int(input())
N=int(input())
a=list(map(int,input().split()))
M=int(input())
b=list(map(int,input().split()))
mb=defaultdict(int)
s=0
for i in range(M):
    s=0
    for j in range(i,M):
        s+=b[j]
        mb[s]+=1
ac=[0 for _ in range(N+1)]
res=0
for i in range(N):
    s=0
    for j in range(i,N):
        s+=a[j]
        if T-s in mb:
            res+=mb[T-s]
print(res)
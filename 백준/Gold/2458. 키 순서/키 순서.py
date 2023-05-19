import sys
import heapq
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
v=[[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    v[b][a]=1
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if v[i][k] and v[k][j]:
                v[i][j]=1
res=0
for i in range(1,N+1):
    cnt=1
    for j in range(1,N+1):
        if v[i][j] or v[j][i]:
            cnt+=1
    if cnt==N:
        res+=1
print(res)
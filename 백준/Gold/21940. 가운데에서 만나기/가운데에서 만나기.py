import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N,M=map(int,input().split())
a=[[987654321 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    q,w,e=map(int,input().split())
    a[q][w]=e
K=int(input())
b=list(map(int,input().split()))
for i in range(1,N+1):
    a[i][i]=0
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if a[i][k]+a[k][j]<a[i][j]:
                a[i][j]=a[i][k]+a[k][j]
res1=987654321
v=[]
for i in range(1,N+1):
    s=0
    for cur in b:
        s=max(s,a[i][cur]+a[cur][i])
    if res1>=s:
        if res1>s:v.clear()
        res1=s
        v.append(i)
print(*v)
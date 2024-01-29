import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
# map(int,input().split())
INF = sys.maxsize
N=int(input())
a=list(map(int,input().split()))
ll=[0 for _ in range(N+1)]
rr=[0 for _ in range(N+1)]
for i in range(N):
    if a[i]>0:
        ll[a[i]]+=1
    else:
        rr[-a[i]]+=1


l=[0 for _ in range(N+1)]
r=[0 for _ in range(N+2)]
for i in range(1,N+1):
    l[i]=l[i-1]+rr[i-1]
for i in range(N-1,-1,-1):
    r[i]=r[i+1]+ll[i+1]
v=[]
for i in range(N+1):
    if (l[i]+r[i])==i:
        v.append(i)
print(len(v))
print(*v)

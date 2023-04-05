import sys
def input():return sys.stdin.readline().rstrip()
arr=[0 for _ in range(50001)]
d=[0 for _ in range(50001)]
N,K,Q,M=map(int,input().split())
k=set(list(map(int,input().split())))
q=list(map(int,input().split()))
for cur in q:
    if cur in k:continue
    for i in range(cur,50000,cur):
        if i in k:continue
        arr[i]=1
for i in range(50000):
    d[i]+=d[i-1]+arr[i]

for i in range(M):
    a,b=map(int,input().split())
    print((b-(a-1))-(d[b]-d[a-1]))